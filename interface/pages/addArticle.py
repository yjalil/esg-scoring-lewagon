import streamlit as st
import requests


st.set_page_config(
    page_title="Add an article",
    page_icon="👋",
)

st.write("# Test our models on a single article")

st.markdown(
    """
    For model testing only the article body text is needed. If the user is satisfied with the ouptut the article can be added to the database. 
    An article must have the following fields not empty :
    * Title
    * Date
    * Source
    * Body
"""
)

body = st.text_area('Text to analyze', '''Your text here''')
response = requests.post("http://127.0.0.1:8000/article/predict/",json={'body':body})

st.markdown("""--------------------------------------------------------------""")
try :
    st.write('Category:', response.json()['topic_category'])
except :
    st.write('Category : Nothing to score yet')

try: 
    st.write('Sentiment score:', response.json()['esg_score'])
except:
    st.write('Sentiment score : Nothing to score yet')



st.markdown("""--------------------------------------------------------------""")

title = st.text_input('Article title')
date = st.text_input('Article date')
company = st.text_input('Company name')
source = st.text_input('Article source')

if st.button('Send to database'):
    response = requests.post("/article/add/test_company_articles_1",json={
        "date": date,
        "title": title,
        "uploaded_at": "2023-01-23T13:24:37.843Z",
        "body": "string with more than 10 characters",
        "sourceURL": "WWW.string.com/stroyURL",
        "topic_category": "TES",
        "esg_score": 0,
        "scored_at": "2023-01-23T13:24:37.843Z",
        "exclude_count": 0
    })
