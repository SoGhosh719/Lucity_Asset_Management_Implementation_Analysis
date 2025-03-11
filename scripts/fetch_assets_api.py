import requests
import pandas as pd

# API details (replace with actual URL and API Key)
API_URL = "https://lucity-api-url.com/assets"
API_KEY = "your_api_key"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

# Fetch asset data
response = requests.get(API_URL, headers=headers)
if response.status_code == 200:
    data = response.json()
    assets_df = pd.DataFrame(data)
    assets_df.to_csv("data/live_assets.csv", index=False)
    print("Live asset data fetched and saved!")
else:
    print("Error fetching asset data:", response.status_code)
