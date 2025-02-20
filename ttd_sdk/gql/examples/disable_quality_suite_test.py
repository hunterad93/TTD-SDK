import json
import os
from dotenv import load_dotenv
from ttd_sdk.gql.client import TTDGraphQLClient

def disable_quality_suite(client: TTDGraphQLClient, ad_group_id: str) -> None:
    print(f"\nAttempting to disable Quality Suite for ad group: {ad_group_id}")
    
    variables = {
        "id": ad_group_id
    }
    
    response = client.execute_query(
        query_name="DisableQualitySuite",
        variables=variables
    )
    
    if "errors" in response:
        print("Mutation failed:", response["errors"])
        return
        
    result = response.get("data", {}).get("adGroupUpdate", {}).get("data", {})
    
    # Print results
    print("\nResults:")
    print(f"Ad Group ID: {ad_group_id}")
    print(f"Quality Alliance Suite Enabled: {result.get('isQualityAllianceSuiteEnabled')}")
    
    # Write full response to JSON file
    output_file = "disable_quality_suite_result.json"
    with open(output_file, "w") as f:
        json.dump(response, f, indent=2)
    print(f"\nFull results written to {output_file}")

def main():
    load_dotenv()
    api_key = os.getenv("TTD_API_KEY")
    if not api_key:
        raise ValueError("TTD_API_KEY environment variable is required")
    
    # You can set this as an environment variable or hardcode for testing
    test_ad_group_id = '7pqpgrf'
    
    # Create client without context manager
    client = TTDGraphQLClient(
        api_key=api_key,
        sandbox=False,
        log_level="DEBUG"
    )
    
    try:
        disable_quality_suite(client, test_ad_group_id)
    finally:
        # Clean up if needed
        pass

if __name__ == "__main__":
    main() 