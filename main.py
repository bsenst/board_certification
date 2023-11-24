import streamlit as st
import pandas as pd
import kaggle
import os

def download_dataset(dataset_path, destination_path):
    try:
        # Download the dataset using Kaggle API
        kaggle.api.dataset_download_files(dataset_path, path=destination_path, unzip=True)
    except Exception as e:
        st.error(f"Failed to download the dataset: {e}")

st.title("Private Kaggle Dataset Access")

# Set Kaggle credentials for this session
os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]

# Specify your dataset path and destination
dataset_path = "bnzn261029/medilearn-qembed"
destination_path = "data"

dataset_downloaded = 0

if st.button("Download Dataset"):
    # Download the dataset using the Kaggle API
    data =download_dataset(dataset_path, destination_path)

    st.success("Dataset downloaded successfully.")
    
    dataset_downloaded = 1

if dataset_downloaded:

    data = pd.read_csv("data/medilearn_qembed.csv")

    data
