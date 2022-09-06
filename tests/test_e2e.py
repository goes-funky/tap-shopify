from integrations_testing_framework import *
import tap_shopify
import os
import pytest
import json

config_path = os.path.abspath('../sample_config.json')


def select_schema(
        catalog_path: str, stream_name: str, stream_key: str = 'stream', select_by_property=None, exclude= None) -> str:
    """
    Creates a catalog file with the stream_name selected.
    Example: @with_sys_args(['--config', config_path, '--catalog', utils.select_schema('all-streams.json', 'epics')])

    :param str catalog_path: a path of a catalog
    :param str stream_name: the name of the stream to be modified
    :param str stream_key: the key that is using for stream dict to select the desired stream
    :param select_by_property : True , when need to select : true each property metadata
    :return: the path of the catalog created as string
    :rtype: str
    """
    f = open(catalog_path, "r")
    catalog = f.read()
    f.close()

    catalog = json.loads(catalog)

    # Selected : True added on each property metadata
    # Add select_property = True as parameter
    if select_by_property is True:
        for stream in catalog['streams']:
            if stream[stream_key] == stream_name:
                for property in stream['metadata']:
                    # Exclude some properties in schema metadata
                    if exclude is not None:
                        if exclude in property['metadata'] or exclude in property['breadcrumb']:
                            pass
                        else:
                            property['metadata']['selected'] = True
                    else:
                        property['metadata']['selected'] = True

    # Selected: True added on the metadata of the stream
    else:
        for stream in catalog['streams']:
            if stream[stream_key] == stream_name:
                stream['metadata'][0]['metadata']['selected'] = True

    # Open the file for writing.
    f = open(f"catalogs/{stream_name}.json", "w")
    f.write(json.dumps(catalog))
    f.close()

    return f"catalogs/{stream_name}.json"


@pytest.mark.skip()  # Currently failing due to a timezone issue
@assert_stdout_matches('streams.json')
@intercept_requests('requests/discovery.txt', generate=False)
@with_sys_args(['--config', config_path, '--discover'])
def test_schema():
    tap_shopify.main()


@assert_stdout_matches('responses/abandoned_checkouts.txt')
@intercept_requests('requests/abandoned_checkouts.txt', generate=False)
# @write_stdout('responses/abandoned_checkouts.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'abandoned_checkouts')])
def test_abandoned_checkouts():
    tap_shopify.main()


@assert_stdout_matches('responses/balance_transactions.txt')
@intercept_requests('requests/balance_transactions.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'balance_transactions')])
def test_balance_transactions():
    tap_shopify.main()


@pytest.mark.skip()  # Currently failing due to a timezone issue
@assert_stdout_matches('responses/collects.txt')
@intercept_requests('requests/collects.txt', generate=True)
# @write_stdout('responses/collects.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'collects')])
def test_collects():
    tap_shopify.main()


@assert_stdout_matches('responses/custom_collections.txt')
@intercept_requests('requests/custom_collections.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'custom_collections')])
def test_custom_collections():
    tap_shopify.main()


@assert_stdout_matches('responses/customer_journey.txt')
@intercept_requests('requests/customer_journey.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'customer_journey')])
def test_customer_journey():
    tap_shopify.main()


@assert_stdout_matches('responses/customers.txt')
@intercept_requests('requests/customers.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'customers')])
def test_customers():
    tap_shopify.main()


@assert_stdout_matches('responses/discount_codes.txt')
@intercept_requests('requests/discount_codes.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'discount_codes')])
def test_discount_codes():
    tap_shopify.main()


@assert_stdout_matches('responses/giftcards.txt')
@intercept_requests('requests/giftcards.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'giftcards')])
def test_giftcards():
    tap_shopify.main()


@assert_stdout_matches('responses/inventory_items.txt')
@intercept_requests('requests/inventory_items.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'inventory_items')])
def test_inventory_items():
    tap_shopify.main()


@assert_stdout_matches('responses/inventory_levels.txt')
@intercept_requests('requests/inventory_levels.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'inventory_levels')])
def test_inventory_levels():
    tap_shopify.main()


@assert_stdout_matches('responses/locations.txt')
@intercept_requests('requests/locations.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'locations')])
def test_locations():
    tap_shopify.main()


# TODO
# @assert_stdout_matches('responses/metafields.txt')
# @intercept_requests('requests/metafields.txt', generate=True)
# @write_stdout('responses/metafields.txt', )
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'metafields')])
# def test_metafields():
#     tap_shopify.main()


@assert_stdout_matches('responses/metafields_custom_collections.txt')
@intercept_requests('requests/metafields_custom_collections.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'metafields_custom_collections')])
def test_metafields_custom_collections():
    tap_shopify.main()


# TODO
# @assert_stdout_matches('responses/metafields_customers.txt')
# @intercept_requests('requests/metafields_customers.txt', generate=True)
# @write_stdout('responses/metafields_customers.txt', )
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'metafields_customers')])
# def test_metafields_customers():
#     tap_shopify.main()


@assert_stdout_matches('responses/metafields_orders.txt')
@intercept_requests('requests/metafields_orders.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'metafields_orders')])
def test_metafields_orders():
    tap_shopify.main()


@assert_stdout_matches('responses/metafields_products.txt')
@intercept_requests('requests/metafields_products.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'metafields_products')])
def test_metafields_products():
    tap_shopify.main()


@assert_stdout_matches('responses/metafields_ql.txt')
@intercept_requests('requests/metafields_ql.txt', generate=False)
# @write_stdout('responses/metafields_ql.txt', )
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'metafields_ql')])
def test_metafields_ql():
    tap_shopify.main()


@assert_stdout_matches('responses/order_refunds.txt')
@intercept_requests('requests/order_refunds.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'order_refunds')])
def test_order_refunds():
    tap_shopify.main()


# @pytest.mark.skip()  # Currently failing
@assert_stdout_matches('responses/orders.txt')
@intercept_requests('requests/orders.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'orders')])
def test_orders():
    tap_shopify.main()


@assert_stdout_matches('responses/payouts.txt')
@intercept_requests('requests/payouts.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'payouts')])
def test_payouts():
    tap_shopify.main()


@assert_stdout_matches('responses/price_rules.txt')
@intercept_requests('requests/price_rules.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'price_rules')])
def test_price_rules():
    tap_shopify.main()


@assert_stdout_matches('responses/products.txt')
@intercept_requests('requests/products.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'products')])
def test_products():
    tap_shopify.main()


@assert_stdout_matches('responses/transactions.txt')
@intercept_requests('requests/transactions.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'transactions')])
def test_transactions():
    tap_shopify.main()
