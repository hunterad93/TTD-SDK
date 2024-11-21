import asyncio
import os
from ttd_sdk.gql.client import TTDGraphQLClient

async def get_live_advertisers():
    # Get API key from environment variable
    api_key = os.getenv("TTD_API_KEY")
    if not api_key:
        raise ValueError("TTD_API_KEY environment variable is required")
        
    partner_id = os.getenv("TTD_PARTNER_ID")
    if not partner_id:
        raise ValueError("TTD_PARTNER_ID environment variable is required")

    async with TTDGraphQLClient(
        api_key=api_key,
        sandbox=True,
        log_level="DEBUG"
    ) as client:
        result = await client.execute_query(
            "GetLiveAdvertiserIds",
            variables={"id": partner_id}
        )
        
        # Print results
        if "errors" in result:
            print("Error:", result["errors"])
            return
            
        advertisers = result["data"]["partner"]["advertisers"]["nodes"]
        live_advertisers = [a for a in advertisers if a["isWithLiveCampaigns"]]
        
        print(f"Total advertisers: {len(advertisers)}")
        print(f"Live advertisers: {len(live_advertisers)}")
        print("\nFirst few live advertisers:")
        for adv in live_advertisers[:5]:
            print(f"- {adv['id']}")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(get_live_advertisers())
