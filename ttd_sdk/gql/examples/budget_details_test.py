import asyncio
import json
from datetime import datetime, timezone
import os
from dotenv import load_dotenv
from ttd_sdk.gql.client import TTDGraphQLClient

async def get_budget_details(client: TTDGraphQLClient, advertiser_id: str) -> None:
    variables = {
        "id": advertiser_id,
        "endDate": datetime.now(timezone.utc).isoformat(),
        "page_size": 25
    }
    
    response = await client.fetch_all(
        query_name="GetAdvertiserBudgetDetails",
        variables=variables
    )
    
    if "errors" in response:
        print("Query failed:", response["errors"])
        return
        
    advertiser = response.get("data", {}).get("advertiser", {})
    campaigns = advertiser.get("campaigns", {}).get("nodes", [])
    
    if not campaigns:
        print(f"No active campaigns found for advertiser ID: {advertiser_id}")
        return
    
    # Collect summary statistics
    campaign_count = len(campaigns)
    flight_count = sum(
        len(campaign.get("flights", {}).get("nodes", [])) 
        for campaign in campaigns
    )
    adgroup_count = sum(
        len(campaign.get("adGroups", {}).get("nodes", [])) 
        for campaign in campaigns
    )
    
    print(f"\nResults Summary:")
    print(f"Found {campaign_count} active campaigns")
    print(f"Total flights: {flight_count}")
    print(f"Total ad groups: {adgroup_count}")
    
    # Print detailed sample data
    print("\nSample Campaign Details:")
    for campaign in campaigns[:2]:
        print(f"\nCampaign ID: {campaign['id']}")
        print(f"Budget: ${campaign['budget']['total']:,.2f}")
        print(f"Pacing Mode: {campaign['pacingMode']}")
        
        flights = campaign.get("flights", {}).get("nodes", [])
        print(f"Flights ({len(flights)}):")
        for flight in flights[:2]:
            print(f"  - Flight {flight['id']}")
            print(f"    Budget: ${flight['budgetInAdvertiserCurrency']:,.2f}")
            if flight.get('dailyTargetInAdvertiserCurrency'):
                print(f"    Daily Target: ${flight['dailyTargetInAdvertiserCurrency']:,.2f}")
            print(f"    Days Remaining: {flight['daysRemaining']}")
        
        adgroups = campaign.get("adGroups", {}).get("nodes", [])
        print(f"Ad Groups ({len(adgroups)}):")
        for adgroup in adgroups[:2]:
            print(f"  - Ad Group {adgroup['id']}")
            print(f"    Base Bid: ${adgroup['baseBidCPMInAdvertiserCurrency']:,.2f}")
            print(f"    Budget: ${adgroup['budget']['total']:,.2f}")
            print(f"    Spend: ${adgroup['spend']['spend']:,.2f}")
            print(f"    Risk Level: {adgroup['spend']['riskLevel']}")
    
    # Write full results to JSON file
    output_file = "budget_details.json"
    with open(output_file, "w") as f:
        json.dump(response, f, indent=2)
    print(f"\nFull results written to {output_file}")

async def main():
    load_dotenv()
    api_key = os.getenv("TTD_API_KEY")
    if not api_key:
        raise ValueError("TTD_API_KEY environment variable is required")
        
    advertiser_id = "l0hmuul"  # Hardcoded advertiser ID
    
    async with TTDGraphQLClient(
        api_key=api_key,
        sandbox=True,
        log_level="DEBUG"  # Enable debug logging to see pagination in action
    ) as client:
        await get_budget_details(client, advertiser_id)

if __name__ == "__main__":
    asyncio.run(main())