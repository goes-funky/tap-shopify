import datetime
import tap_shopify
import pytest
from freezegun import freeze_time
from integrations_testing_framework import *


config_path = os.path.abspath('./sample_config.json')


@pytest.mark.skip()
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


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/balance_transactions.txt')
@intercept_requests('tests/requests/balance_transactions.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
    'tests/streams.json', 'balance_transactions', 'stream')])
def test_balance_transactions():
    tap_shopify.main()


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
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
    'tests/streams.json', 'customers', 'stream')])
def test_customers():
    tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/giftcards.txt')
@intercept_requests('tests/requests/giftcards.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/streams.json', 'giftcards', 'stream')])
def test_giftcards():
    tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/inventory_items.txt')
@intercept_requests('tests/requests/inventory_items.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
    'tests/streams.json', 'inventory_items', 'stream')])
def test_inventory_items():
    tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@write_stdout('tests/responses/inventory_levels.txt')
@intercept_requests('tests/requests/inventory_levels.txt', generate=True)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
    'tests/streams.json', 'inventory_levels', 'stream')])
def test_inventory_levels():
    tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/locations.txt')
@intercept_requests('tests/requests/locations.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/streams.json', 'locations', 'stream')])
def test_locations():
    tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/metafields_custom_collections.txt')
@intercept_requests('tests/requests/metafields_custom_collections.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema(
    'tests/streams.json', 'metafields_custom_collections', 'stream')])
def test_metafields_custom_collections():
    tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/payouts.txt')
@intercept_requests('tests/requests/payouts.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/streams.json', 'payouts', 'stream')])
def test_payouts():
    tap_shopify.main()


@freeze_time(datetime.datetime.strptime("2022-09-08T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
@assert_stdout_matches('tests/responses/products.txt')
@intercept_requests('tests/requests/products.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/streams.json', 'products', 'stream')])
def test_products():
    tap_shopify.main()

