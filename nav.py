import  data_viz, stats
import streamlit as st

PAGES = {'Data Visualization': data_viz,
        'Statistical Analysis': stats}

selected = st.sidebar.radio('Select Page:',['Data Visualization','Statistical Analysis'])
page = PAGES[selected]

page.app()