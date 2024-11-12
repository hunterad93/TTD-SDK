import os
from pathlib import Path
from dotenv import load_dotenv

# Get the project root directory (2 levels up from this file)
root_dir = Path(__file__).parent.parent.parent
env_path = root_dir / '.env'

# Load the .env file from the root directory
load_dotenv(env_path)

from ttd_sdk.client import TTDClient

# Initialize client (use sandbox=True for testing)
client = TTDClient(sandbox=True)

# Make API calls
response = client.get("/adgroup/v10v8mq")
print(response)