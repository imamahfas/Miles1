import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def app():
    st.header('Statistical Analysis')

    @st.cache(allow_output_mutation=True)
    def load_data(nrows):
        data = pd.read_csv('h8dsft_P0ML1_Imam_Ahfas.csv', nrows=nrows)
        
        return data


    
    data = load_data(100000)
    
    data['profit'] = data['retail_price'] - data['cost']

#### fig 5 ####

    Male = data[data['gender']=='M'].profit
    fig5, ax5 = plt.subplots()
    sns.boxplot(Male)
    st.pyplot(fig5)
    st.caption('Profit average of sales by Male with Tukeys Rule')

#### fig 6 ###

    Q1 = 12.93150025 
    Q2 = 21.43777088 
    Q3 = 36.41900008
    IQR = Q3-Q1
    IQR
    Maximum = Q3 + (3 * IQR)
    Maximum
    df_Male = data[data['gender']=='M'] 
    Outlier_atas = df_Male[df_Male['profit']>Maximum]['profit']
    Outlier_atas

    df_Outlier = df_Male[
            (~df_Male['profit'].isin(Outlier_atas)) 
    ]
    df_Outlier.head(2)
    Male_Uji= df_Outlier.profit

    t_stat,p_val = stats.ttest_1samp(Male_Uji, 32.439959)

    pop = np.random.normal(Male_Uji.mean(), Male_Uji.std(), 10000)

    # confidence interval with critical value 0.05
    ci = stats.norm.interval(0.95, Male_Uji.mean(), Male_Uji.std())

    # memvisualisasikan simulasi pdf
    fig, ax = plt.subplots(figsize=(16,5))
    sns.histplot(pop, label='Rata-rata profit pembelian Male tanpa outlier', color='blue', kde=True, stat="density", linewidth=0)
    ax.axvline(Male_Uji.mean(), color='red', linewidth=2, label='Rata-rata profit pembelian Male tanpa outlier (Mean)')

    # Visualisasikan garis rata2 dari data yang sudah disiapkan di awal
    # mean
    ax.axvline(Male_Uji.mean(), color='red', linewidth=2, label='Male product profit mean')

    # membuat garis confidence interval
    ax.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
    ax.axvline(ci[0], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')

    # membuat garis p-value/alternative hypotesis
    ax.axvline(pop.mean() + t_stat*pop.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis/p-value')
    ax.axvline(pop.mean() - t_stat*pop.std(), color='black', linestyle='dashed', linewidth=2)
    st.pyplot(fig)
    st.caption('Profit average of sales by Male with TTest 1 sample 2 tailed analysis')