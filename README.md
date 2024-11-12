# TTD-SDK

Python SDK for streamlining future interactions with the Trade Desk's platform API.

See general documentation here:
[Getting Started with the API Platform](https://partner.thetradedesk.com/v3/portal/api/doc/ApiPlatformGetStarted)

## Overview

This SDK consists of a client plus model and resource modules for each API entity. To use, include an `.env` file with:
- `TTD_USERNAME`
- `TTD_PASSWORD`
- `TTD_PARTNER_ID`

I chose to focus on basic get, create, put, and list methods for each entity and will add support for 'get by name' methods, query facet methods, or other special methods that are available for various resources as needed.

There are occasionally multiple 'list' methods for an entity included if they all seem useful.

## Supported Entities

The following entities are supported by this SDK:

- Activity Logs - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/Activity%20Log)
- Ad Groups - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/Ad%20Group)
- Advertisers - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/Advertiser)
- App Event Trackers - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/App%20Event%20Tracker)
- Audiences - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/Audience)
- Campaigns - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/Campaign)
- Creatives - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/Creative)
- Data Groups - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/Data%20Group)
- First Party Data Elements - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/First%20Party%20Data)
- Third Party Data Elements - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/Third%20Party%20Data)
- Universal Pixels - [Documentation](https://partner.thetradedesk.com/v3/portal/api/area/Universal%20Pixel)

## TODO
- Add support for 'get by name' methods with campaigns and ad groups
- Add support for additional fees related methods