import datetime
import tap_shopify
from freezegun import freeze_time
from integrations_testing_framework import *


config_path = os.path.abspath('./sample_config.json')


@assert_stdout_matches('tests/streams.json')
@intercept_requests('tests/requests/discovery.txt', generate=False)
@with_sys_args(['--config', config_path, '--discover'])
def test_schema():
    tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/abandoned_checkouts.txt')
@intercept_requests('tests/requests/abandoned_checkouts.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
    'tests/streams.json', 'abandoned_checkouts', 'stream')])
def test_abandoned_checkouts():
    tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('tests/responses/balance_transactions.txt')
# @intercept_requests('tests/requests/balance_transactions.txt', generate=True)
# @with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
#     'tests/streams.json', 'balance_transactions', 'stream')])
# def test_balance_transactions():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('tests/responses/collects.txt')
# @intercept_requests('tests/requests/collects.txt', generate=True)
# @with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/streams.json', 'collects', 'stream')])
# def test_collects():
#     tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/custom_collections.txt')
@intercept_requests('tests/requests/custom_collections.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
    'tests/streams.json', 'custom_collections', 'stream')])
def test_custom_collections():
    tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/customer_journey.txt')
@intercept_requests('tests/requests/customer_journey.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
    'tests/streams.json', 'customer_journey', 'stream')])
def test_customer_journey():
    tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/customers.txt')
@intercept_requests('tests/requests/customers.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/streams.json', 'customers', 'stream')])
def test_customers():
    tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('tests/responses/discount_codes.txt')
# @intercept_requests('tests/requests/discount_codes.txt', generate=True)
# @with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
#     'tests/streams.json', 'discount_codes', 'stream')])
# def test_discount_codes():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('tests/responses/giftcards.txt')
# @intercept_requests('tests/requests/giftcards.txt', generate=True)
# @with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/streams.json', 'giftcards', 'stream')])
# def test_giftcards():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('tests/responses/inventory_items.txt')
# @intercept_requests('tests/requests/inventory_items.txt', generate=True)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('tests/streams.json', 'inventory_items', 'stream')])
# def test_inventory_items():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('tests/responses/inventory_levels.txt')
# @intercept_requests('tests/requests/inventory_levels.txt', generate=True)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('tests/streams.json', 'inventory_levels', 'stream')])
# def test_inventory_levels():
#     tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/locations.txt')
@intercept_requests('tests/requests/locations.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/streams.json', 'locations', 'stream')])
def test_locations():
    tap_shopify.main()

# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('tests/responses/metafields.txt')
# @intercept_requests('tests/requests/metafields.txt', generate=True)
# @write_stdout('tests/responses/metafields.txt', )
# @with_sys_args(['--config', config_path, '--catalog', select_schema('tests/streams.json', 'metafields', 'stream')])
# def test_metafields():
#     tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/metafields_custom_collections.txt')
@intercept_requests('tests/requests/metafields_custom_collections.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
    'tests/streams.json', 'metafields_custom_collections', 'stream')])
def test_metafields_custom_collections():
    tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('tests/responses/metafields_customers.txt')
# @intercept_requests('tests/requests/metafields_customers.txt', generate=True)
# @write_stdout('tests/responses/metafields_customers.txt', )
# @with_sys_args(['--config', config_path, '--catalog', select_schema('tests/streams.json', 'metafields_customers', 'stream')])
# def test_metafields_customers():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('responses/metafields_orders.txt')
# @intercept_requests('requests/metafields_orders.txt', generate=True)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'metafields_orders')])
# def test_metafields_orders():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('responses/metafields_products.txt')
# @intercept_requests('requests/metafields_products.txt', generate=True)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'metafields_products')])
# def test_metafields_products():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('responses/metafields_ql.txt')
# @intercept_requests('requests/metafields_ql.txt', generate=True)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'metafields_ql')])
# def test_metafields_ql():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @assert_stdout_matches('responses/order_refunds.txt')
# @intercept_requests('requests/order_refunds.txt', generate=False)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'order_refunds')])
# def test_order_refunds():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @assert_stdout_matches('responses/orders.txt')
# @intercept_requests('requests/orders.txt', generate=False)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'orders')])
# def test_orders():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('responses/payouts.txt')
# @intercept_requests('requests/payouts.txt', generate=True)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'payouts')])
# def test_payouts():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @assert_stdout_matches('responses/price_rules.txt')
# @intercept_requests('requests/price_rules.txt', generate=False)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'price_rules')])
# def test_price_rules():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @assert_stdout_matches('responses/products.txt')
# @intercept_requests('requests/products.txt', generate=False)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'products')])
# def test_products():
#     tap_shopify.main()


# @freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
# @write_stdout('responses/transactions.txt')
# @intercept_requests('requests/transactions.txt', generate=False)
# @with_sys_args(['--config', config_path, '--catalog', select_schema('streams.json', 'transactions')])
# def test_transactions():
#     tap_shopify.main()
