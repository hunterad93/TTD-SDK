import asyncio
import json
import os
from dotenv import load_dotenv
from ttd_sdk.gql.client import TTDGraphQLClient

async def get_advertiser_budget_details(client: TTDGraphQLClient) -> None:
    variables = {
        "page_size": 10
    }
    
    response = await client.fetch_all(
        query_name="GetAdvertiserBudgetDetails",
        variables=variables
    )
    
    if "errors" in response:
        print("Query failed:", response["errors"])
        return
        
    advertisers = response.get("data", {}).get("advertisers", {}).get("nodes", [])
    
    if not advertisers:
        print("No advertisers found")
        return
    
    # Print summary statistics
    total_count = len(advertisers)
    live_campaigns_count = sum(1 for adv in advertisers if adv.get("isWithLiveCampaigns"))
    
    print(f"\nResults Summary:")
    print(f"Total advertisers found: {total_count}")
    print(f"Advertisers with live campaigns: {live_campaigns_count}")
    
    # Print sample data
    print("\nSample Advertiser Details:")
    for advertiser in advertisers[:5]:  # Show first 5 advertisers
        print(f"\nAdvertiser ID: {advertiser['id']}")
        print(f"Has Live Campaigns: {advertiser['isWithLiveCampaigns']}")
    
    # Write full results to JSON file
    output_file = "advertiser_budget_details.json"
    with open(output_file, "w") as f:
        json.dump(response, f, indent=2)
    print(f"\nFull results written to {output_file}")

async def main():
    load_dotenv()
    api_key = os.getenv("TTD_API_KEY")
    if not api_key:
        raise ValueError("TTD_API_KEY environment variable is required")
    
    async with TTDGraphQLClient(
        api_key=api_key,
        sandbox=False,
        log_level="DEBUG"  # Enable debug logging to see pagination in action
    ) as client:
        await get_advertiser_budget_details(client)

if __name__ == "__main__":
    asyncio.run(main())