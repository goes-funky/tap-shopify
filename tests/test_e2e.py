
from integrations_testing_framework import *
import tap_shipstation
import os
import pytest

config_path = os.path.abspath('config.json')

@pytest.mark.skip() # Currently failing due to a timezone issue
@assert_stdout_matches('tests/catalog.json')
@intercept_requests('tests/requests/discovery.txt', generate=True)
@with_sys_args(['--config', config_path, '--discover'])
def test_schema():
    tap_shipstation.main()

# @write_stdout('tests/responses/abandoned_checkouts.txt')
@assert_stdout_matches('tests/responses/abandoned_checkouts.txt')
@intercept_requests('tests/requests/abandoned_checkouts.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'carriers')])
def test_carriers():
    tap_shipstation.main()


# @write_stdout('tests/responses/customers.txt')
@assert_stdout_matches('tests/responses/customers.txt')
@intercept_requests('tests/requests/customers.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'customers')])
def test_customers():
    tap_shipstation.main()

# @write_stdout('tests/responses/marketplaces.txt')
@assert_stdout_matches('tests/responses/marketplaces.txt')
@intercept_requests('tests/requests/marketplaces.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'marketplaces')])
def test_marketplaces():
    tap_shipstation.main()

# @write_stdout('tests/responses/orders.txt')
@assert_stdout_matches('tests/responses/orders.txt')
@intercept_requests('tests/requests/orders.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'orders')])
def test_orders():
    tap_shipstation.main()

# @write_stdout('tests/responses/products.txt')
@assert_stdout_matches('tests/responses/products.txt')
@intercept_requests('tests/requests/products.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'products')])
def test_products():
    tap_shipstation.main()

# @write_stdout('tests/responses/store_info.txt')
@assert_stdout_matches('tests/responses/store_info.txt')
@intercept_requests('tests/requests/store_info.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'store_info')])
def test_store_info():
    tap_shipstation.main()

# @write_stdout('tests/responses/users.txt')
@assert_stdout_matches('tests/responses/users.txt')
@intercept_requests('tests/requests/users.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'users')])
def test_users():
    tap_shipstation.main()

# @write_stdout('tests/responses/warehouses.txt')
@assert_stdout_matches('tests/responses/warehouses.txt')
@intercept_requests('tests/requests/warehouses.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'warehouses')])
def test_warehouses():
    tap_shipstation.main()

# @write_stdout('tests/responses/webhook.txt')
@assert_stdout_matches('tests/responses/webhook.txt')
@intercept_requests('tests/requests/webhook.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'webhook')])
def test_webhooks():
    tap_shipstation.main()

# @write_stdout('tests/responses/fulfillments.txt')
@assert_stdout_matches('tests/responses/fulfillments.txt')
@intercept_requests('tests/requests/fulfillments.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'fulfillments')])
def test_fulfillments():
    tap_shipstation.main()

# @write_stdout('tests/responses/packages.txt')
@assert_stdout_matches('tests/responses/packages.txt')
@intercept_requests('tests/requests/packages.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'packages')])
def test_packages():
    tap_shipstation.main()

# @write_stdout('tests/responses/packages.txt')
@assert_stdout_matches('tests/responses/packages.txt')
@intercept_requests('tests/requests/packages.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'packages')])
def test_packages():
    tap_shipstation.main()

# @write_stdout('tests/responses/shipments.txt')
@assert_stdout_matches('tests/responses/shipments.txt')
@intercept_requests('tests/requests/shipments.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'shipments')])
def test_shipments():
    tap_shipstation.main()

# @write_stdout('tests/responses/stores.txt')
@assert_stdout_matches('tests/responses/stores.txt')
@intercept_requests('tests/requests/stores.txt', generate=False)
@with_sys_args(['--config', config_path, '--catalog', utils.select_schema('tests/catalog.json', 'stores')])
def test_stores():
    tap_shipstation.main()

