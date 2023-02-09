import streamlit as st
import requests
import json
import pandas as pd

st.set_page_config(page_title="Cleaning database", page_icon="📈")


tuple_companies = []
response = requests.get("http://127.0.0.1:8000/companies/").json()
for JSONcompany in response :
    tuple_companies.append(JSONcompany['name']) 

st.markdown("# Company Articles")
st.sidebar.header("Company Articles")
st.write(
    """You can delete articles that might seem problematic"""
)

start_date = st.date_input('Start date')
end_date = st.date_input('End date')
company = st.selectbox(
    'Company',
    tuple(tuple_companies))

if st.button('Show Articles'):
                            #   http://127.0.0.1:8000/articles/byCompany/detailed/Tesla/Period/2010-01-01/2023-02-08
    response = requests.get(f"http://127.0.0.1:8000/articles/byCompany/detailed/{company}/Period/{start_date}/{end_date}")
    
    for article in response.json():
        with st.expander(label = f"{article['id']} : {article['date']} | {article['title']})"):
            st.markdown(f"[Read more]({article['sourceURL']})")
            st.metric(label="Topic", value=article['topic_category'])
            st.metric(label="Sentiment", value=article['esg_score'])
            if st.button(label="Delete Article", key = f"Delete Article {article['id']}"):
                requests.delete(f"http://127.0.0.1:8000/article/delete/{article['id']}")
            if st.button(label="Flag for Retraining", key = f"Flag for Retraining {article['id']}"):
                requests.patch(f"http://127.0.0.1:8000/article/flag/{article['id']}")
