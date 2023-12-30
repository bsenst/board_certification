import streamlit as st
import pandas as pd
import kaggle
import os
import utils

st.subheader("Medical Board Certification Questions")

st.warning("The questions and answers displayed are for learning purposes only.")

utils.load_data()

fachdisziplin_options = sorted(st.session_state["pruefungsprotokolle"].Fachdisziplin.dropna().unique())
fachdisziplin_choosen = st.selectbox("Choose Fachdisziplin", fachdisziplin_options)

# get doc id for choosen fachdisziplin and limit cluster accordingly
doc_id = st.session_state["pruefungsprotokolle"][st.session_state["pruefungsprotokolle"].Fachdisziplin==fachdisziplin_choosen].index.values
questions = st.session_state["questions"][st.session_state["questions"].doc_id.isin(doc_id)]
cluster_options = questions.cluster.unique().tolist()
len_cluster = len(cluster_options)

# choose clusters
cluster_choosen = cluster_options[st.select_slider(
    "Choose Cluster",
    options = [i for i in range(1,len(cluster_options))],
    format_func = lambda x: ''
)]

# return final questions
questions = questions[questions.cluster==cluster_choosen]
output = list(questions.questions)

st.write(f"Cluster: {cluster_choosen}, number of questions: {len(questions)}")

if len(output)>10:
    output = output[:5]

for i, question in enumerate(output):
    st.write(i+1, question)
