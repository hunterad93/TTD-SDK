# Query Formatting Guide for TTD GraphQL Client

## Basic Rules for Paginated Queries

1. **Cursor Variable Naming**
   - Name cursor variables based on the path to the paginated field
   - Format: `{field_path}_cursor`
   - Example: `campaigns_flights_cursor` for flights nested under campaigns

2. **Required Structure for Paginated Fields**
   ```graphql
   field(
       first: $page_size,
       after: $field_cursor,
       where: { /* optional filters */ }
   ) {
       nodes {
           # field data
       }
       pageInfo {
           hasNextPage
           endCursor
       }
   }
   ```

## Example Query

```graphql
query GetCampaignAndAdGroupFlightsExample(
    $id: ID = "",
    $campaigns_cursor: String,
    $campaigns_flights_cursor: String,
    $page_size: Int = 25
) {
    advertiser(id: $id) {
        id
        name
        campaigns(first: $page_size, after: $campaigns_cursor) {
            nodes {
                id
                name
                flights(first: $page_size, after: $campaigns_flights_cursor) {
                    nodes {
                        id
                        startDateInclusiveUTC
                        endDateExclusiveUTC
                    }
                    pageInfo {
                        hasNextPage
                        endCursor
                    }
                }
            }
            pageInfo {
                hasNextPage
                endCursor
            }
        }
    }
}
```

## Usage with Client

```python
variables = {
    "id": "advertiser_id",
    "page_size": 25
}

# Client will automatically handle pagination
response = await client.fetch_all(
    query_name="GetCampaignAndAdGroupFlightsExample",
    variables=variables
)
```

## Key Requirements

1. **Variable Naming**
   - Cursor variables must follow the path pattern: `parent_child_cursor`
   - Include `page_size` variable with a default value

2. **Field Structure**
   - Every paginated field needs:
     - `nodes` array containing the items
     - `pageInfo` object with `hasNextPage` and `endCursor`
   - Include cursor and page size parameters: `first: $page_size, after: $cursor`

3. **Response Handling**
   - Client automatically detects paginated fields
   - Merges all pages into a single response
   - Maintains nested structure of data

## Notes

- The client handles all pagination automatically
- No need to manually track cursors
- Works with any depth of nested pagination
- Supports additional filter parameters in queries