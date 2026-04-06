#==============================================
#STEP 0: Import necessary libraries
#==============================================

import requests
import json
import pandas as pd

#==============================================
#STEP 1: Import API key from key.env
#==============================================

import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_API_KEY = os.environ.get("DATABASE_API_KEY")

#==============================================
#STEP 2: Make API request to NASA Exoplanet Archive
#==============================================

query_params = {
    "query": "SELECT pl_name,hostname,ra,dec FROM ps WHERE disc_facility LIKE '%Kepler%'",
    "format": "json"
}
headers = {
    "Authorization": f"Bearer {DATABASE_API_KEY}"
}
response = requests.get(
    url="https://exoplanetarchive.ipac.caltech.edu/TAP/sync", params=query_params, headers=headers
)
print(response.status_code)

#==============================================
#STEP 3: Process the response and convert to DataFrame
#==============================================

data = response.json()
print(type(data))
#df = pd.DataFrame(data)
#print(df.head())

#==============================================