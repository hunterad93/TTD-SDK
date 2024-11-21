import asyncio
import json
from pathlib import Path
from client import TTDGraphQLClient

async def fetch_schema(api_key: str):
    async with TTDGraphQLClient(api_key) as client:
        response = await client.execute_query("introspection", variables={})
        
        if response.data:
            schema_json = {
                "__schema": {
                    "types": response.data.types,
                    "queryType": response.data.queryType,
                    "mutationType": response.data.mutationType,
                    "subscriptionType": response.data.subscriptionType
                }
            }
            
            with open("schema.graphql", "w") as f:
                json.dump(schema_json, f, indent=2)
            print("Schema saved to schema.graphql")
        else:
            print("Error fetching schema:", response.errors)

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()
    api_key = os.getenv("TTD_API_KEY")
    asyncio.run(fetch_schema(api_key))