import asyncio
import json
import os
from dotenv import load_dotenv
from ttd_sdk.gql.client import TTDGraphQLClient

async def get_quality_suite_details(client: TTDGraphQLClient) -> None:
    variables = {
        "page_size": 1000
    }
    
    response = await client.fetch_all(
        query_name="GetQualitySuite",
        variables=variables
    )
    
    if "errors" in response:
        print("Query failed:", response["errors"])
        return
        
    ad_groups = response.get("data", {}).get("adGroups", {}).get("nodes", [])
    
    if not ad_groups:
        print("No ad groups found")
        return
    
    # Print summary statistics
    total_count = len(ad_groups)
    enabled_count = sum(1 for ag in ad_groups if ag.get("isEnabled"))
    qas_enabled_count = sum(1 for ag in ad_groups if ag.get("isQualityAllianceSuiteEnabled"))
    
    print(f"\nResults Summary:")
    print(f"Total ad groups found: {total_count}")
    print(f"Enabled ad groups: {enabled_count}")
    print(f"Quality Alliance Suite enabled: {qas_enabled_count}")
    
    # Print sample data
    print("\nSample Ad Group Details:")
    for ad_group in ad_groups[:5]:  # Show first 5 ad groups
        print(f"\nAd Group ID: {ad_group['id']}")
        print(f"Enabled: {ad_group['isEnabled']}")
        print(f"Quality Alliance Suite Enabled: {ad_group['isQualityAllianceSuiteEnabled']}")
    
    # Write full results to JSON file
    output_file = "quality_suite_details.json"
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
        await get_quality_suite_details(client)

if __name__ == "__main__":
    asyncio.run(main())