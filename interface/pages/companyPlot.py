import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Plotting Company ESG trend", page_icon="📈")

st.markdown("# Company Plot")
st.sidebar.header("Company Plot")
st.write(
    """You can pick a company from the dropdown menu from all available Moroccan companies in our database. Pick a start and end date for a period to plot."""
)

