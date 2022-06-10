import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title('Thelook_Ecommerce')
    st.subheader('Dashboard Visualization')
    st.write('by Imam Ahfas FTDS Batch 12')
   

    @st.cache(allow_output_mutation=True)
    def load_data(nrows):
        data = pd.read_csv('h8dsft_P0ML1_Imam_Ahfas.csv', nrows=nrows)
        
        return data


   
    data = load_data(75000)
    


    ##### fig 1 ####
    data['profit'] = data['retail_price'] - data['cost']
    st.write(data)
    df_profit = data[data['status']=='Complete']
    a = df_profit.groupby(['status'])[['cost','retail_price', 'profit']].sum().T
    fig, ax = plt.subplots()
    sns.barplot(data = a, x = a.index, y = 'Complete', ax = ax)
    st.pyplot(fig)
    st.caption('Profit sales of thelook_ecommerce')

    #### fig 2 ####
    d = data[data['status']=='Complete']['category'].value_counts()
    dx = pd.DataFrame(d)
    fig4, ax4 = plt.subplots()
    sns.barplot(data = dx, x = dx.index, y = 'category', ax = ax4)
    plt.xticks(rotation=90)
    st.pyplot(fig4)
    st.caption('Sales by profuct category of thelook_ecommerce')

    #### fig 3 ####
    b = data[data['status']=='Complete']['city'].value_counts().head().T
    bc = pd.DataFrame(b)
    fig2, ax2 = plt.subplots()
    sns.barplot(data = bc, x = bc.index, y = b , ax = ax2)
    st.pyplot(fig2)
    st.caption('Sales by city of user origin of thelook_ecommerce')

    #### fig 4 ####
    c = data[data['status']=='Complete']['gender'].value_counts().head().T
    cx = pd.DataFrame(c)
    fig3, ax3 = plt.subplots()
    sns.barplot(data = cx, x = cx.index, y = c , ax = ax3)
    st.pyplot(fig3)
    st.caption('sales by gender of thelook_ecommerce')

def new_func():
    return 100000

   

    