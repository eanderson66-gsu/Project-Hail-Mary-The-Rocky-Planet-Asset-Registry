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

#==============================================
#STEP 2: Make API request to NASA Exoplanet Archive
#==============================================

query_params = {
    "query": "SELECT pl_name,hostname,ra,dec,pl_rade,pl_bmasse,st_teff,sy_dist FROM ps WHERE disc_facility LIKE '%Kepler%'",
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

#==============================================
#STEP 3: Process the response and convert to DataFrame
#==============================================

data = response.json()
print(type(data))

#==============================================

#==============================================
#STEP 4: Convert JSON data to pandas DataFrame and display the first few rows
#==============================================

df = pd.DataFrame(data)
print(df.head())

#==============================================

#==============================================
#STEP 5: Perform integrity checks on the data and Drop any rows with missing values
#==============================================

print(df.isnull().sum())

cols_to_check = ['pl_bmasse', 'pl_rade', 'sy_dist']
df_cleaned = df.dropna(subset=cols_to_check)


print(f"Mission-Ready Assets: {len(df_cleaned)}")

#==============================================

#==============================================
#STEP 6: Calculate the Relative Surface Gravity for each exoplanet and add it as a new column in the DataFrame
#==============================================

df_cleaned['gravity'] = df_cleaned['pl_bmasse'] / (df_cleaned['pl_rade']**2)

#==============================================

#==============================================
#STEP 7: reate a new Boolean column (True/False) called habitable
#==============================================

df_cleaned['habitable'] = (df_cleaned['gravity'] >= 0.8) & (df_cleaned['gravity'] <= 1.2) & (df_cleaned['sy_dist'] <= 100).astype(bool)
print(df_cleaned['habitable'].sum())
df_test = df_cleaned[df_cleaned['habitable'] == True]
print(df_test['habitable'].sum())
#==============================================