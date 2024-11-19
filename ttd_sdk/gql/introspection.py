import asyncio
from pathlib import Path
from client import TTDGraphQLClient

async def fetch_schema(api_key: str):
    print(f"Using API key: {api_key[:5]}...")  # Show first 5 chars of API key
    
    async with TTDGraphQLClient(api_key) as client:
        print("\nExecuting introspection query...")
        response = await client.execute_query("introspection", variables={})
        
        if response.data:
            with open("schema.graphql", "w") as f:
                f.write(str(response.data))
            print("\nSchema saved to schema.graphql")
        else:
            print("\nError fetching schema:", response.errors)

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()
    api_key = os.getenv("TTD_API_KEY")
    if not api_key:
        print("Error: No TTD_API_KEY found in environment")
        exit(1)
    asyncio.run(fetch_schema(api_key))