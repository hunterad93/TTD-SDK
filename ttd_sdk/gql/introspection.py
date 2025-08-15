import asyncio
import json
import sys
from pathlib import Path

# Add the parent directory to the path so we can import the SDK
sys.path.insert(0, str(Path(__file__).parent.parent))

from ttd_sdk.gql.client import TTDGraphQLClient

def fetch_schema(api_key: str):
    # TTDGraphQLClient is not async, so remove async/await
    with TTDGraphQLClient(api_key) as client:
        # You'll need to create an introspection query first
        introspection_query = """
        query IntrospectionQuery {
          __schema {
            types {
              name
              kind
              description
              fields {
                name
                type {
                  name
                  kind
                }
              }
            }
            queryType {
              name
            }
            mutationType {
              name
            }
            subscriptionType {
              name
            }
          }
        }
        """
        
        response = client.execute_user_query(introspection_query)
        
        if "data" in response and response["data"]:
            schema_json = response["data"]
            
            with open("schema.json", "w") as f:
                json.dump(schema_json, f, indent=2)
            print("Schema saved to schema.json")
        else:
            print("Error fetching schema:", response.get("errors"))

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()
    api_key = os.getenv("TTD_API_KEY")
    
    # Remove asyncio since the client is synchronous
    fetch_schema(api_key)