import streamlit as st
import requests
import json
import pandas as pd

st.set_page_config(page_title="Plotting Company ESG trend", page_icon="📈")


tuple_companies = []
response = requests.get("http://127.0.0.1:8000/companies/").json()
for JSONcompany in response :
    tuple_companies.append(JSONcompany['name']) 

st.markdown("# Company Plot")
st.sidebar.header("Company Plot")
st.write(
    """You can pick a company from the dropdown menu from all available Moroccan companies in our database. Pick a start and end date for a period to plot."""
)



start_date = st.date_input('Start date')
end_date = st.date_input('End date')
company = st.selectbox(
    'Company',
    tuple(tuple_companies))

if st.button('Plot'):
    response_plot = requests.get(f"http://127.0.0.1:8000/articles/byCompany/{company}/Period/{start_date}/{end_date}")
    df = pd.DataFrame(response_plot.json())
    
    df_env = df[df['topic_category']=='Environmental'].copy()
    df_env['Env_cumul'] = df_env['esg_score'].cumsum()
    df_soc = df[df['topic_category']=='Social'].copy()
    df_soc['Soc_cumul'] = df_soc['esg_score'].cumsum()
    df_gov = df[df['topic_category']=='Governance'].copy()
    df_gov['Gov_cumul'] = df_gov['esg_score'].cumsum()
    st.write(f"Total articles found : None: {len(df)-(len(df_env)+len(df_soc)+len(df_gov))}, Env : {len(df_env)}, Soc : {len(df_soc)}, Gov : {len(df_gov)}")
    st.write('Enviromental records :')
    st.dataframe(df_env)
    st.write('Social records :')
    st.dataframe(df_soc)
    st.write('Governance records :')
    st.dataframe(df_gov)
    
    
