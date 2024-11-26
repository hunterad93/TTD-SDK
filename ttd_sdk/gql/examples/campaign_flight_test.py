import asyncio
import json
import os
from dotenv import load_dotenv
from ttd_sdk.gql.client import TTDGraphQLClient

async def get_campaign_flights(client: TTDGraphQLClient, advertiser_id: str) -> None:
    variables = {
        "id": advertiser_id,
        "page_size": 25
    }
    
    response = await client.fetch_all(
        query_name="GetCampaignAndAdGroupFlightsExample",
        variables=variables
    )
    
    if "errors" in response:
        print("Query failed:", response["errors"])
        return
        
    advertiser = response.get("data", {}).get("advertiser", {})
    if not advertiser:
        print(f"No advertiser found with ID: {advertiser_id}")
        return
        
    campaigns = advertiser.get("campaigns", {}).get("nodes", [])
    campaign_count = len(campaigns)
    flight_count = sum(len(campaign.get("flights", {}).get("nodes", [])) for campaign in campaigns)
    
    print(f"\nResults Summary:")
    print(f"Found {campaign_count} campaigns with {flight_count} total flights")
    
    # Print some sample data
    print("\nFirst few campaigns and their flights:")
    for campaign in campaigns[:3]:
        flight_count = len(campaign.get("flights", {}).get("nodes", []))
        print(f"\nCampaign: {campaign['name']} ({campaign['id']})")
        print(f"Total flights: {flight_count}")
        if flight_count > 0:
            print("Sample flights:")
            for flight in campaign["flights"]["nodes"][:2]:
                print(f"- Flight {flight['id']}: {flight['startDateInclusiveUTC']} to {flight['endDateExclusiveUTC']}")
    
    # Write full results to JSON file
    output_file = "campaign_flights.json"
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
        await get_campaign_flights(client, advertiser_id)

if __name__ == "__main__":
    asyncio.run(main())