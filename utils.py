import json
import gspread
import pandas as pd
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials

def connect_gsheet():
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(st.secrets["keys"]), scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)

    return client
