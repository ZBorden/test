import json
import logging
import os
import pandas as pd
import requests
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint as pprint

logging.basicConfig(level=logging.INFO)
load_dotenv()

DOMO_PLANNING_REPORT = os.getenv('domo_planning_amount')
current_month = datetime.now().strftime('%m-%d-%Y')
# current_month = date.year
logging.info(f"Current Month: {current_month}")

def fetch_redash_query_results():
    df = pd.read_csv(DOMO_PLANNING_REPORT)
    pprint(df)
    
    df.to_csv('Domo_Monthly_Data.csv', index=False)

fetch_redash_query_results()

