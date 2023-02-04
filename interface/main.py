import streamlit as st

st.set_page_config(
    page_title="ESG Advisor",
    page_icon="👋",
)

st.write("# ESG advisor based on NLP technics ")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    Our ESG tool is based on 2 NLP models. The first model can read and classify articles by topic. It outputs 4 categories :
    * Environmental
    * Social
    * Governance
    * None
    The second model is based on Vader sentiment analysis and can assign a sentiment score to the article. On this stage all articles classified as "None" are ignored.
    We run a cumulative sum on the sentiments to plot a time series curve for each company.
"""
)
