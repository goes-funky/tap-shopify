import shopify

from tap_shopify.context import Context
from tap_shopify.streams.base import Stream


class Location(Stream):
    name = 'locations'
    replication_object = shopify.Location
    key_properties = []
    replication_method = 'FULL_TABLE'

    def get_objects(self):
        return self.replication_object.find()


Context.stream_objects['locations'] = Location
