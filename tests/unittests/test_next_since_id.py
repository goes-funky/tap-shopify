from types import SimpleNamespace

from tap_shopify.streams.base import get_next_since_id


def objs(*ids):
    return [SimpleNamespace(id=i) for i in ids]


def test_ordered_page_uses_last_id():
    assert get_next_since_id(objs(10, 11, 12), 1) == 12


def test_out_of_order_tail_is_refetched():
    # Two orders created in the same second, returned with ids swapped
    # (6967441719639 is #6020223, 6967441686871 is #6020224).
    page = objs(6967441600000, 6967441719639, 6967441686871)
    assert get_next_since_id(page, 1) == 6967441686870


def test_no_progress_falls_back_to_max_id():
    assert get_next_since_id(objs(12, 10, 11), 9) == 12


def test_since_id_paging_does_not_skip_or_fail_with_swapped_ids():
    # Simulated API: returns ids > since_id, ordered by (created_at, order_number)
    # instead of id, which swaps ids 3 and 4 created in the same second at the
    # end of the first page.
    records = [(1, 0, 1), (2, 1, 2), (4, 2, 3), (3, 2, 4), (5, 3, 5), (6, 4, 6), (7, 5, 7)]
    limit = 4

    def call_api(since_id):
        rows = sorted((r for r in records if r[0] > since_id), key=lambda r: (r[1], r[2]))
        return objs(*[r[0] for r in rows[:limit]])

    seen, since_id = set(), 0
    while True:
        page = call_api(since_id)
        seen.update(o.id for o in page)
        if len(page) < limit:
            break
        since_id = get_next_since_id(page, since_id)

    assert seen == {r[0] for r in records}


class FakePage(list):
    """Mimics shopify.collection.PaginatedCollection."""

    def __init__(self, items, next_page_url=None, fetch=None):
        super().__init__(items)
        self.next_page_url = next_page_url
        self._fetch = fetch

    def next_page(self, no_cache=False):
        return self._fetch(self.next_page_url)


def test_stream_follows_cursor_with_swapped_ids(monkeypatch):
    from tap_shopify.context import Context
    from tap_shopify.streams.base import Stream
    import tap_shopify.streams.base as base

    # The two orders from the incident: created in the same second, returned
    # by Shopify ordered by order number instead of id.
    ids = [6967441600000, 6967441719639, 6967441686871, 6967441800000, 6967441900000]
    limit = 2

    def page(offset):
        url = offset + limit if offset + limit < len(ids) else None
        return FakePage(objs(*ids[offset:offset + limit]), url, page)

    class FakeResource:
        @staticmethod
        def find(**kwargs):
            return page(0)

    class FakeStream(Stream):
        name = "orders"
        replication_object = FakeResource

    monkeypatch.setattr(Context, "config", {"start_date": "2025-10-27T00:00:00Z"}, raising=False)
    monkeypatch.setattr(Context, "state", {}, raising=False)
    monkeypatch.setattr(Context, "get_results_per_page", staticmethod(lambda default: limit))
    monkeypatch.setattr(base.singer.utils, "now",
                        lambda: base.utils.strptime_with_tz("2025-10-28T00:00:00Z"))
    monkeypatch.setattr(base.singer, "write_state", lambda state: None)

    assert [o.id for o in FakeStream().get_objects()] == ids
