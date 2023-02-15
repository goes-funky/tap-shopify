import datetime

import shopify
import singer
from gql_query_builder import GqlQuery
from singer import utils

from tap_shopify.context import Context
from tap_shopify.streams.base import Stream
from tap_shopify.streams.graph_ql_stream import GraphQlStream

LOGGER = singer.get_logger()


class ProductsQL(GraphQlStream):
    name = 'products'

    replication_object = shopify.Product
    prefix = 'gid://shopify/Products/'
    status_key = "published_status"

    def get_table_schema(self) -> dict:
        streams = Context.catalog["streams"]
        schema = None
        for stream in streams:
            if stream["tap_stream_id"] == "products_ql":
                schema = stream["schema"]
                break

        return schema

    def get_graph_edges(self) -> str:
        fields = self.get_graph_ql_prop(self.get_table_schema())
        node = GqlQuery().fields(fields, name='node').generate()
        edges = GqlQuery().fields(['cursor', node], name='edges').generate()
        return edges

    def get_graph_ql_prop(self, schema: dict) -> list:
        properties = schema["properties"]
        ql_fields = []
        for prop_name in properties:
            prop_obj = properties[prop_name]
            prop_type = prop_obj["type"]

            if "generated" in prop_type:
                continue

            if 'object' in prop_type:
                if prop_obj["properties"]:
                    fields = self.get_fragment_fields(prop_name, self.get_graph_ql_prop(prop_obj))
                    ql_field = GqlQuery().fields(fields, name=prop_name).generate()
                    ql_fields.append(ql_field)

            elif 'array' in prop_type:
                if prop_obj["items"]["properties"]:
                    fields = self.get_fragment_fields(prop_name, self.get_graph_ql_prop(prop_obj["items"]))
                    ql_field = GqlQuery().fields(fields, name=prop_name).generate()
                    if prop_name in self.need_edges_cols:
                        node = GqlQuery().fields(fields, name='node').generate()
                        edges = GqlQuery().fields([node], "edges").generate()
                        ql_field = GqlQuery().query(prop_name, input={
                            "first": 5
                        }).fields([edges]).generate()

                    ql_fields.append(ql_field)
            else:
                if prop_name in list(self.fragment_cols):
                    fragment_entity = self.fragment_cols[prop_name]
                    fields = self.get_fragment_fields(prop_name, self.fragment_entities[fragment_entity])
                    ql_field = GqlQuery().fields(fields, name=prop_name).generate()
                    ql_fields.append(ql_field)
                    continue

                # used to extract id from object inside main object
                # if prop_name in list(self.selection_fields):
                #     selected_field = GqlQuery().fields(["id"], name=prop_name).generate()
                #     ql_fields.append(selected_field)
                #     continue

                ql_fields.append(prop_name)
        return ql_fields

    def get_graph_ql_data(self, replication_obj: Stream):
        LOGGER.info("Getting data with GraphQL")
        updated_at_min = replication_obj.get_bookmark()

        today_date = singer.utils.now().replace(microsecond=0)
        stop_time = today_date
        date_window_size = float(Context.config.get("date_window_size", 100))

        # Retrieve data for max 1 year. Otherwise log incremental needed.
        diff_days = (stop_time - updated_at_min).days
        yearly = False
        records = 0
        if diff_days > 365:
            yearly = True
            stop_time = updated_at_min + datetime.timedelta(days=365)
            LOGGER.info("This import will only import the first year of historical data. "
                        "You need to trigger further incremental imports to get the missing rows.")

        max_time = 1
        started_at = datetime.datetime.now()
        # Page through till the end of the result set
        while updated_at_min < stop_time and (datetime.datetime.now() - started_at).days < max_time:
            after = None
            updated_at_max = updated_at_min + datetime.timedelta(days=date_window_size)

            if updated_at_max > stop_time:
                updated_at_max = stop_time
            singer.log_info("getting from %s - %s", updated_at_min,
                            updated_at_max)
            while True:
                # Check if import start time until now exceeds max allowed hours
                run_days = (datetime.datetime.now() - started_at).days
                if run_days > max_time:
                    LOGGER.info("Import time of %s day(s) exceeds allowed max days %s. "
                                "Please trigger further incremental data to get the missing rows.",
                                int(run_days), max_time)
                    break

                query = self.get_graph_query(updated_at_min,
                                             updated_at_max,
                                             replication_obj.name,
                                             after=after)
                data = self.excute_graph_ql(query)
                data = data[replication_obj.name]
                page_info = data['pageInfo']
                edges = data["edges"]
                node = {}

                for edge in edges:
                    after = edge["cursor"]
                    node = edge["node"]
                    records += len(node)
                    yield node

                if not page_info["hasNextPage"]:
                    Context.state.get('bookmarks', {}).get(replication_obj.name, {}).pop('since_id', None)
                    replication_obj.update_bookmark(utils.strftime(updated_at_max + datetime.timedelta(seconds=1)))
                    break

            updated_at_min = updated_at_max + datetime.timedelta(seconds=1)

            # count records and add additional window size time if no data found
            if not records and stop_time < today_date:
                stop_time += datetime.timedelta(days=date_window_size)

        if yearly:
            LOGGER.info("This import only imported one year of historical data. "
                        "Please trigger further incremental data to get the missing rows.")
Context.stream_objects['products_ql'] = ProductsQL
