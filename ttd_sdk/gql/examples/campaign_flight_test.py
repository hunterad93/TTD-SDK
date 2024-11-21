import asyncio
import json
import os
from dotenv import load_dotenv
from ttd_sdk.gql.client import TTDGraphQLClient

async def get_campaign_flights(client: TTDGraphQLClient, advertiser_id: str) -> None:
    variables = {
        "id": advertiser_id
    }
    
    response = await client.execute_query("GetCampaignAndAdGroupFlightsExample", variables)
    
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
    
    print(f"Found {campaign_count} campaigns with {flight_count} total flights")
    
    # Write full results to JSON file
    output_file = "campaign_flights.json"
    with open(output_file, "w") as f:
        json.dump(response, f, indent=2)
    print(f"Full results written to {output_file}")

async def main():
    load_dotenv()
    api_key = os.getenv("TTD_API_KEY")
    advertiser_id = "jc1xp06"
    

    
    async with TTDGraphQLClient(api_key) as client:
        await get_campaign_flights(client, advertiser_id)

if __name__ == "__main__":
    asyncio.run(main())