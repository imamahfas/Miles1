import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.header('DATA VISUALIZATION')
    st.write('by Imam Ahfas FTDS Batch 12')
    st.title('Dashboard Thelook_Ecommerce')

    @st.cache
    def load_data(nrows):
        data = pd.read_csv('h8dsft_P0ML1_Imam_Ahfas.csv', nrows=nrows)
        
        return data


    data_load_state = st.text('Loading data...')
    data = load_data(75000)
    data_load_state.text("Done! (using st.cache)")
    ##### fig 1 ####
    data['profit'] = data['retail_price'] - data['cost']
    st.write(data)
    df_profit = data[data['status']=='Complete']
    a = df_profit.groupby(['status'])[['cost','retail_price', 'profit']].sum().T
    fig, ax = plt.subplots()
    sns.barplot(x=x, y=y)
    sns.barplot(data = a, x = a.index, y = 'Complete', ax = ax)
    st.pyplot(fig)

    #### fig 2 ####
    d = data[data['status']=='Complete']['category'].value_counts()
    dx = pd.DataFrame(d)
    fig4, ax4 = plt.subplots()
    sns.barplot(x=x, y=y)
    sns.barplot(data = dx, x = dx.index, y = 'category', ax = ax4)
    plt.xticks(rotation=90)
    st.pyplot(fig4)

    #### fig 3 ####
    b = data[data['status']=='Complete']['city'].value_counts().head().T
    bc = pd.DataFrame(b)
    fig2, ax2 = plt.subplots()
    sns.barplot(x=x, y=y)
    sns.barplot(data = bc, x = bc.index, y = b , ax = ax2)
    st.pyplot(fig2)

    #### fig 4 ####
    c = data[data['status']=='Complete']['gender'].value_counts().head().T
    cx = pd.DataFrame(c)
    fig3, ax3 = plt.subplots()
    sns.barplot(x=x, y=y)
    sns.barplot(data = cx, x = cx.index, y = c , ax = ax3)
    st.pyplot(fig3)

def new_func():
    return 100000

   

    