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

st.subheader("Medical Board Certification Questions")

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

columns_to_read = ['doc_id', 'questions', 'cluster']
questions = pd.read_csv(st.secrets["file1"], usecols=columns_to_read)
questions = questions.drop_duplicates()

columns_to_read = ['Fachdisziplin']
pruefungsprotokolle = pd.read_csv(st.secrets["file2"], usecols=columns_to_read)

fachdisziplin_options = pruefungsprotokolle.Fachdisziplin.unique()
fachdisziplin = st.selectbox("Choose Fachdisziplin:", fachdisziplin_options)
cluster = st.slider("Cluster", questions.cluster.min(), questions.cluster.max(), value=183)

doc_ids = pruefungsprotokolle[pruefungsprotokolle.Fachdisziplin==fachdisziplin].index

output = questions[questions.cluster==cluster]
output = output[output.doc_id.isin(doc_ids)]

st.write("Number of questions:", len(output))

output = list(output.questions)

if len(output)>10:
    output = output[:5]

for i, question in enumerate(output):
    st.write(i+1, question)