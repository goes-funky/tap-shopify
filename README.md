# Shopify

This tap pulls raw data from [Shopify](https://shopify.dev/api/admin-rest)


## Supported Features
| Feature Name                                                                            | Supported | Comment |
| ------------                                                                            |---------|---------|
| [Full Import](https://docs.y42.com/docs/features#full-import)                           | ✅        |         |
| [Partial Import](https://docs.y42.com/docs/features#partial-import)                     | ✅      |         |
| [Start Date Selection](https://docs.y42.com/docs/features#start-date-selection)         | ✅      |         |
| [Import Empty Tables](https://docs.y42.com/docs/features#import-empty-table)            | ❌      |         |
| [Custom Data](https://docs.y42.com/docs/features#custom-data)                           | ❌      |         |
| [Retroactive Updating](https://docs.y42.com/docs/features#retroactive-updating)         | ❌      |         |
| [Dynamic Column Selection](https://docs.y42.com/docs/features#dynamic-column-selection) | ✅      |         |      


## Connector

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

### Supported Streams

| Name                                                                              | Description                                                                                                                                                                     | Stream Type  |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [Abandoned Checkouts](https://shopify.dev/api/admin-rest/2022-01/resources/abandoned-checkouts) | Information on customers who have abandoned their carts/ checkouts                                                                                                              | INCREMENTAL  |
| [Balance Transactions](https://shopify.dev/api/admin-rest/2022-07/resources/transactions)       | Every single movement of money in or out of the account is recorded here                                                                                                        | INCREMENTAL  |
| [Collects](https://shopify.dev/api/admin-rest/2022-01/resources/collect)   | The relationship between products and custom collections                                                                                                                        | INCREMENTAL  |
| [Custom Collections](https://shopify.dev/api/admin-rest/2022-01/resources/customcollection)     | A grouping of products that a merchant can create to make their store easier to browse                                                                                          | INCREMENTAL  |
| [Customer Journey]()                |                                                                                                                                                                                 | INCREMENTAL  |
| [Customers](https://shopify.dev/api/admin-rest/2022-01/resources/customer)  | Stores information about a shop's customers, such as their contact details, their order history, and whether they've agreed to receive email marketing.                         | INCREMENTAL  |
| [Discount Codes](https://shopify.dev/api/admin-rest/2022-01/resources/discountcode) | Belongs to a price rules, which holds the logic for the discount to be redeemed.                                                                                                | INCREMENTAL  |      
| [Giftcards](https://shopify.dev/api/admin-graphql/2022-01/objects/GiftCard) | Requires read_gift_cards access scope. Also: The API client must be a private or custom app installed on a Shopify Plus or Shopify Plus Partner Sandbox store.                  | INCREMENTAL  |      
| [Inventory Items](https://shopify.dev/api/admin-rest/2022-01/resources/inventoryitem) | Represents a physical good with its essential information holding SKU and whether its inventory is tracked.                                                                     | INCREMENTAL  |      
| [Inventory Levels](https://shopify.dev/api/admin-rest/2022-01/resources/inventorylevel) | Represents the quantities of an inventory item for a location.                                                                                                                  | INCREMENTAL  |      
| [Locations](https://shopify.dev/api/admin-rest/2022-01/resources/location) | Represents a geographical location where your stores, pop-up stores, headquarters, and warehouses exist.                                                                        | INCREMENTAL  |      
| [Metafields](https://shopify.dev/api/admin-rest/2022-01/resources/metafield) | A flexible way to attach additional information to a Shopify resource, for example specifications, size charts, downloadable documents, release dates, images, or part numbers. | INCREMENTAL  |      
| [Metafields Custom Collections](https://shopify.dev/api/admin-rest/2022-01/resources/metafield) | A flexible way to attach additional information to custom collections                                                                                                           | INCREMENTAL  |      
| [Metafields Customers](https://shopify.dev/api/admin-rest/2022-01/resources/metafield) | A flexible way to attach additional information to customers                                                                                                                    | INCREMENTAL  |      
| [Metafields Orders](https://shopify.dev/api/admin-rest/2022-01/resources/metafield) | A flexible way to attach additional information to orders                                                                                                                       | INCREMENTAL  |      
| [Metafields Products](https://shopify.dev/api/admin-rest/2022-01/resources/metafield) | A flexible way to attach additional information to products                                                                                                                     | INCREMENTAL  |      
| [Order Refunds](https://shopify.dev/api/admin-rest/2022-01/resources/refund) | Returned orders                                                                                                                                                                 | INCREMENTAL  |      
| [Orders](https://shopify.dev/api/admin-rest/2022-01/resources/order) | An order is a customer's request to purchase one or more products from a shop.                                                                                                  | INCREMENTAL  |      
| [Payouts](https://shopify.dev/api/admin-rest/2022-01/resources/payouts) | Represent the movement of money between a Shopify Payments account balance and a connected bank account.                                                                        | INCREMENTAL  |      
| [Price Rules](https://shopify.dev/api/admin-rest/2022-07/resources/pricerule) | Rules on prices such as discount application                                                                                                                                    | INCREMENTAL  |      
| [Products](https://shopify.dev/api/admin-rest/2022-01/resources/product) | A item/ service offered for sale                                                                                                                                                | INCREMENTAL  |      
| [Transactions](https://shopify.dev/api/admin-rest/2022-01/resources/transaction) | Transactions are created for every order that results in an exchange of money.                                                                                                  | INCREMENTAL  |      
| [Transactions](https://shopify.dev/api/admin-rest/2022-01/resources/transaction) | Transactions are created for every order that results in an exchange of money.                                                                                                  | INCREMENTAL  |      


  - Outputs the schema for each resource
  - Incrementally pulls data based on the input state
  - When Metafields are selected, this tap will sync the Shopify store's top-level Metafields and any additional Metafields for selected tables that also have them (ie: Orders, Products, Customers)


### Workflow

User authenticates through credentials of his own private app and gets data for a store per integration. Data is retrieved using 2 request types: REST & GraphQL.
For both of them, there is a yearly timeframe set on sync where the query is repeated by incrementing inside this timeframe with a configured daily window size.
If there is no data in the initial sync, the calendar year timeframe will be expanded until first record occurred.

> Quotas 

- Per app, per store:

| API                    | Rate-limiting method | Standard limit    | Shopify Plus limit  |
|------------------------|----------------------|-------------------|---------------------|
| [Admin API (GraphQL)]() | Calculated query cost | 50 points/second  | 100 points/second   |
| [Admin API (REST)]() | Admin API (REST) | 2 requests/second  |  4 requests/second         |
| | Admin API (REST) | 40 requests/minute  |  80 requests/minute         |


- Admin API (Rest) Request-based limit:   

second -> 2 Requests per second    
minute -> 40 Requests per minute    

Apps can make a maximum number (2 or 4 requests per second) of requests per minute and 40 API requests within 60 seconds. Each request counts equally, regardless of how much or how little data is returned. 

- Admin API (GraphQL) Calculated query cost: 

minute (app <> store combination) → Total points to use: 1000           
second → Points replenished per Second: +50       

The API supports a maximum of 1000 cost points per app per store per minute. This quota replenishes at a rate of 50 cost points per second.

- Pagination

Max 250 records per page, configured per stream. (Could have also different load depending on stream)



---

## Quick Start

1. Install

    pip install tap-shopify

2. Create the config file

   Create a JSON file called `config.json`. Its contents should look like:

   ```json
    {
        "start_date": "2010-01-01",
        "api_key": "<Shopify API Key>",
        "shop": "test_shop"
    }
    ```

   The `start_date` specifies the date at which the tap will begin pulling data
   (for those resources that support this).

   The `api_key` is the API key for your Shopify shop generated via an OAuth flow.

   The `shop` is your Shopify shop which will be the value `test_shop` in the string `https://test_shop.myshopify.com`

4. Run the Tap in Discovery Mode

    tap-shopify -c config.json -d

   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode).

5. Run the Tap in Sync Mode

    tap-shopify -c config.json --catalog catalog-file.json

---

# How To Setup
## Resources


### Overview
 
**Authentication**: App Credentials     
**Settings**: Historical Date selection     
**Schema type**: Fixed  
**Update Type**: Full import and incremental    


### Authorization and Access

First, you have to specify the subdomain of your Shopify store, e.g. **"yourshopname"** for a Shopify store that has the domain **"http://yourshopname.shopify.com/"**
 
The app authentication for Shopify uses a Admin API token from the custom app that you have created in Shopify. This custom app is strictly isolated to the Shopify in which it was created and can only be used to access data from the account in which they were created. 
 
To read more about custom apps in Shopify, please go [here](https://help.shopify.com/en/manual/apps/custom-apps).
Watch [this](https://www.loom.com/share/f6576d7a7fa2466ba48361c37fa2aa68) video for a step-by-step guide to create a custom app in Shopify for Y42.