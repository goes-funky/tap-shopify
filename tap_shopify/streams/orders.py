import shopify

from tap_shopify.context import Context
from tap_shopify.streams.base import Stream

DEPRECATED_COLUMNS = ["processing_method", ("shipping_lines","delivery_category"), "payment_details", "gateway"]
# DEPRECATED_COLUMNS = ["gateway", "cart_token", ("shipping_lines","delivery_category")]


def _remove_deprecated_entries(record):
    for k in DEPRECATED_COLUMNS:
        if isinstance(k, tuple):
            (k0, k1) = k
            if k0 in record:
                sub_element = record[k0]
                if isinstance(sub_element, list):
                    for s in sub_element:
                        s.pop(k1, None)
                else:
                    sub_element.pop(k1, None)
        else:
            record.pop(k, None)
    return record


class Orders(Stream):
    name = 'orders'
    replication_object = shopify.Order

    def sync(self):
        """Yield's processed SDK object dicts to the caller.

        This is the default implementation. Get's all of self's objects
        and calls to_dict on them with no further processing.
        """
        for obj in self.get_objects():
            record = obj.to_dict()

            record = _remove_deprecated_entries(record)

            record["customer_id"] = record.get("customer") and record["customer"].get("id") or False
            yield record


Context.stream_objects['orders'] = Orders
