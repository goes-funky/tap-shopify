import shopify
import singer
from singer import utils
from tap_shopify.streams.base import (Stream,
                                      RESULTS_PER_PAGE,
                                      OutOfOrderIdsError,
                                      get_next_since_id)
from tap_shopify.context import Context

LOGGER = singer.get_logger()

class Collects(Stream):
    name = 'collects'
    replication_object = shopify.Collect
    replication_key = 'updated_at'

    def get_objects(self):
        since_id = self.get_since_id() or 1
        bookmark = self.get_bookmark()
        max_bookmark = utils.strftime(utils.now())
        self.last_bookmark = bookmark
        while True:
            query_params = {
                "since_id": since_id,
                "limit": RESULTS_PER_PAGE,
            }
            if since_id != 1:
                LOGGER.info("Resuming sync from since_id %d", int(since_id))

            objects = self.call_api(query_params)

            for obj in objects:
                # Syncing Collects is a full sync every time but emitting
                # records that have an updated_date greater than the
                # bookmark
                if not obj.updated_at and obj.id:
                    LOGGER.info('Collect with id: %d does not have an updated_at, syncing it!',
                                obj.id)
                if not obj.updated_at or utils.strptime_with_tz(obj.updated_at) > bookmark:
                    if obj.id < int(since_id):
                        raise OutOfOrderIdsError("obj.id < since_id: {} < {}".format(
                            obj.id, since_id))
                    self.compare_bookmark(obj.updated_at)
                    yield obj

            self.update_bookmark(self.last_bookmark)

            if len(objects) < RESULTS_PER_PAGE:
                # Update the bookmark at the end of the last page
                self.update_bookmark(max_bookmark)
                break

            since_id = get_next_since_id(objects, int(since_id))
            self.push_id(since_id)


Context.stream_objects['collects'] = Collects
