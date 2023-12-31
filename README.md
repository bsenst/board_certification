# Streamlit Q&A Personalized Learning Platform
Use Streamlit to create a learning platform :books: A preview of questions clustered by topic is available in the public area. In the private area (Google Firebase user authentication :closed_lock_with_key:) the learning experience is personalized. The questions and answers can be easily managed by the administrator in Google Sheets :floppy_disk: and are connected to the Streamlit app.

![app-architecture](https://github.com/bsenst/board_certification/assets/8211411/8e535fc7-1649-4940-85b8-f0b8500fb775)

Have a look and try out the public facing and personalized sites of the Streamlit app. To enter the personalized area create an user account and manage your individual content.

[https://medical-board-certification-questions.streamlit.app/](https://medical-board-certification-questions.streamlit.app/)

Medical questions are presented in this use case. The questions have been collected from a web forum of exam protocols. The data was processed on the Kaggle platform translating them into English language, using a Large-Language Model to extract the questions, clustering with k-Means and adding LLM-generated answers that have been curated manually (human-in-the-loop). Use the application for your question and answer collection.

### Sources
* [https://www.kaggle.com/docs/api](https://github.com/Kaggle/kaggle-api)
* [https://github.com/burnash/gspread](https://github.com/burnash/gspread)
* [https://github.com/googleapis/google-api-python-client](https://github.com/googleapis/google-api-python-client)
* [https://github.com/googleapis/oauth2client](https://github.com/googleapis/oauth2client)
* [https://github.com/cmayoracurzio/streamlit_firebase_auth](https://github.com/cmayoracurzio/streamlit_firebase_auth)

### Disclaimer
The questions and answers displayed are for learning purposes only.
