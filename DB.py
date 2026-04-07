#==============================================
#STEP 0: Import necessary libraries
#==============================================

import sqlite3
import pandas as pd
import Project_Petrova_Code as ppc

#==============================================

#==============================================
#STEP 1: Create a connection to the SQLite database and insert the DataFrame into a table
#==============================================

db_path = r'C:\Users\era64\Downloads\GSU Portfolio Projects\Project Petrova Automated Orbital Asset & Thermal Flux Monitoring System\Project_Petrova_DB'

try:
    conn = sqlite3.connect(db_path)
    ppc.df_test.to_sql('mission_assets', conn, if_exists='replace', index=False)
    print("Data inserted into SQLite database successfully.")
except Exception as e:
    print(f"Error occurred while inserting data into SQLite database: {e}")
finally:
    if 'conn' in locals():
        conn.close()

#==============================================
