import os
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

def download_dataset(dataset_path, destination_path):
    try:
        # Download the dataset using Kaggle API
        kaggle.api.dataset_download_files(dataset_path, path=destination_path, unzip=True)
    except Exception as e:
        st.error(f"Failed to download the dataset: {e}")

def load_data():
    # save data locally
    if not os.path.exists("data"):

        # Set Kaggle credentials for this session
        os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
        os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]

        # Specify your dataset path and destination
        dataset_path1 = st.secrets["dataset_path1"]
        dataset_path2 = st.secrets["dataset_path2"]
        destination_path = "data"

        # Download the dataset using the Kaggle API
        download_dataset(dataset_path1, destination_path)
        download_dataset(dataset_path2, destination_path)

        st.success("Dataset downloaded successfully.")

    # load data into session_state
    if "questions" not in st.session_state:
        columns_to_read = ['doc_id', 'questions', 'cluster']
        st.session_state["questions"] = pd.read_csv(st.secrets["file1"], usecols=columns_to_read).drop_duplicates()

    if "pruefungsprotokolle" not in st.session_state:
        columns_to_read = ['Fachdisziplin']
        st.session_state["pruefungsprotokolle"] = pd.read_csv(st.secrets["file2"], usecols=columns_to_read)
