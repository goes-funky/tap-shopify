---
title: Shopify
excerpt: 
category: 62b332e637a6a3004298b8c1
slug: shopify
parentDoc: 62b3332a94695c005a9703a2
---


# Description

The Shopify integration replicates data via the Shopify API. You can find the full list of available objects and tables you are able to import to your Y42 instance on Shopify's API documentation.

For a complete overview, refer to [Shopify API.](https://shopify.dev/api)

***



# Supported Features

_A table listing all possible feature integration can have that we support. Any limitation or specification of that feature is also pointed out here._

| **Feature Name**                                                                        | **Supported** | **Comment**                             |
| --------------------------------------------------------------------------------------- | ------------- | --------------------------------------- |
| [Full Import](https://docs.y42.com/docs/features#full-import)                           | Yes           |                                         |
| [Incremental Import](https://docs.y42.com/docs/features#partial-import)                     | Yes           | Yearly data                             |
| [Start Date Selection](https://docs.y42.com/docs/features#start-date-selection)         | Yes           |                                         |
| [Import Empty Tables](https://docs.y42.com/docs/features#import-empty-table)            | No            | Empty streams will not generate a table |
| [Custom Data](https://docs.y42.com/docs/features#custom-data)                           | No            |                                         |
| [Retroactive Updating](https://docs.y42.com/docs/features#retroactive-updating)         | Yes           | Historical data                         |
| [Dynamic Column Selection](https://docs.y42.com/docs/features#dynamic-column-selection) | Yes           | Select optional, non mandatory columns  |

***



# Sync Overview

_A collection of specifications from the API that affects the import of data. Please, provide details and the reference from the API documentation for each topic. if there is none, just delete the topic._

**Historical Data**

_Is there any limitation on how old we can retrieve data?_

**Real-time data**

_Can we import data in real-time or is there a time window specifying a delay? If yes, is this delay officially supported by the API document, made by us, or reported by customers? _

**Performance Consideration**

_Is there any performance consideration for the API we need to highlight to customers? _

**Edge cases or known limitations**

_Any other specific characteristic of this integration may affect how it works._

**Any API feature we support**

_For example, Amazon has support for each marketplace in each region._

**Recommendations**

_Is there any recommendations for our users, to guarantee they are using this integration in the most efficient way possible._

***



# Connector 

This connector was developed following the standards of the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

### Authentication

_What Auth methods are supported for this source?_

### Rate limits & Pagination

\_Describe the rate limits and refer to the documentation.

\__How pagination works._

***



# Schema

This source is based on the [{API_NAME}]({API_LINK}), and is currently in the version {API_Version}.

## Supported Streams

| **Name**<br>_With hyperlink to the original API reference_                                      | **Description**<br>_What data can be found inside_                 | **Stream Type** <br>_Where this data is from_ | **API & API Version** <br> _Optional, if streams are from multiple APIs_ |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------------ |
| [Abandoned Checkouts](https://shopify.dev/api/admin-rest/2022-01/resources/abandoned-checkouts) | Information on customers who have abandoned their carts/ checkouts | INCREMENTAL                                   |                                                                          |
|                                                                                                 |                                                                    |                                               |                                                                          |
|                                                                                                 |                                                                    |                                               |                                                                          |
