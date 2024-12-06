import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns
import functions
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Sales Data Analysis",
    page_icon="🌟", 
    layout="wide", 
    initial_sidebar_state="expanded" 
)


col1 , col2 , col3 = st.columns([1.3 , 3 , 1])
with col2 :
    st.markdown('## CUSTOMER PERSONA CLASSIFICATION')


col1 , col2 , col3 = st.columns([3 , 2 , 3])
with col2 :
    st.text(
        '''
    PATTERN RECOGNITION PROJECT
    GROUP : 2
    Lead Name : Shrijeet Kumar
    Team Member 1 : 
    Team Member 2 : 
    Team Member 3 : 
    '''
    )


st.markdown("#### Cleaned DataSet : ")
df = pd.read_csv('data\Cleaned_marketing_campaign.csv')
df = functions.transform(df)

st.dataframe(df)

st.write("___")
col1 , col2 = st.columns(2)
with col1 :
    st.markdown("#### What's the age distribution of customers ?")
    df1  = functions.ageDist(df)
    fig, ax = plt.subplots()
    sns.histplot(df1.values, kde=True, ax=ax, color='blue')
    ax.set_title("Age Distribution")
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")
    st.pyplot(fig)

with col2 :
    st.markdown("#### What's the Total Spending distribution of customers ?")
    df1  = functions.TotalSpendingDist(df)
    fig , ax = plt.subplots()
    sns.histplot(df1.values , kde=True, ax=ax, color='blue')
    ax.set_title("Total Spending Distribution")
    ax.set_xlabel("Total_Spending($)")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    
col1 , col2 , col3 = st.columns([3 ,6 , 1])





st.write("____")
with col2:
    st.markdown("#### What's the  correlation between Marital status and total spending?")

col1 , col2 = st.columns(2)
with col1 :
    fig , ax = plt.subplots()
    sns.scatterplot(data=df , x = 'Age' , y = 'Total_Spending' , hue = df['Marital_Status'])
    st.pyplot(fig)

with col2 :
    df1 = functions.maritalStatusTotalSpening(df)
    fig , ax = plt.subplots()
    sns.barplot(x=df1.index , y=df1.values)
    st.pyplot(fig)





st.write("_____")
col1 , col2 , col3 = st.columns([3 ,6 , 1])   
with col2:
    st.markdown("#### What's the  correlation between age and total spending?")

col1 , col2 , col3 = st.columns([1.5 , 5 , 1.5])
with col2 :
    fig , ax = plt.subplots()
    sns.boxplot(data=df, x=pd.cut(df['Age'], bins=[0, 20, 30, 40, 50,60,70,80,130]), y='Total_Spending')
    st.pyplot(fig)




st.write("____")
col1 , col2 , col3 = st.columns([2 ,8 , 1])   
with col2:
    st.markdown("#### How does income level influence purchasing patterns across different product categories?")

col1 , col2 = st.columns([2 , 8])

with col1 :
    st.write('INCOME($)')
    st.dataframe(df["Income"].describe())

with col2 :
    df1 = functions.incomeWIseSpending(df)
    st.dataframe(df1)

    incol1 , incol2  = st.columns(2)
    with incol1:
        df1 = functions.expenVsincomeVsprod(df , 'Low Income')
        labels = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
        fig , ax = plt.subplots()
        plt.pie(df1 ,labels=labels, colors=['brown', 'blue', 'green', 'red', 'pink', 'yellow'], autopct='%1.1f%%', startangle=140)
        plt.title(f"Expenditure Distribution for Low Income", fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        st.pyplot(fig)
    with incol2:
        df1 = functions.expenVsincomeVsprod(df , 'Below Average Income')
        labels = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
        fig , ax = plt.subplots()
        plt.pie(df1 ,labels=labels, colors=['brown', 'blue', 'green', 'red', 'pink', 'yellow'], autopct='%1.1f%%', startangle=140)
        plt.title(f"Expenditure Distribution for Below Average Income", fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        st.pyplot(fig)
    with incol1:
        df1 = functions.expenVsincomeVsprod(df , 'Above Average Income')
        labels = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
        fig , ax = plt.subplots()
        plt.pie(df1 ,labels=labels, colors=['brown', 'blue', 'green', 'red', 'pink', 'yellow'], autopct='%1.1f%%', startangle=140)
        plt.title(f"Expenditure Distribution for Above Average Income", fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        st.pyplot(fig)
    with incol2:
        df1 = functions.expenVsincomeVsprod(df , 'High Income')
        labels = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
        fig , ax = plt.subplots()
        plt.pie(df1 ,labels=labels, colors=['brown', 'blue', 'green', 'red', 'pink', 'yellow'], autopct='%1.1f%%', startangle=140)
        plt.title(f"Expenditure Distribution for High Income", fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        st.pyplot(fig)



st.write("____")
col1 , col2 , col3 = st.columns([2 ,8 , 1])   
with col2:
    st.markdown("#### Is there a relationship between education level and response to marketing campaigns?")
col1 , col2 , col3 = st.columns([1,3, 1])   

with col2:
    df1 = functions.eduVscampaign(df)
    fig , ax = plt.subplots()
    sns.barplot(x=df1.index , y=df1.values)
    st.pyplot(fig)




st.write("____")
col1 , col2 , col3 = st.columns([2 ,8 , 1])   
with col2:
    st.markdown("#### Do households with children/teenagers show different spending patterns compared to those without? ")
col1 , col2= st.columns(2)   

with col1 :
    df1 = functions.famVsTotalSpending(df)
    fig1, ax1 = plt.subplots()
    sns.barplot(x=df1.index, y=df1.values, ax=ax1, color="blue")
    ax1.set_title("Total Spending vs Family Type")
    ax1.set_xlabel("Family Type")
    ax1.set_ylabel("Total Spending")
    plt.xticks(rotation=90)
    st.pyplot(fig1)

with col2 :
    df2 = functions.famVsTypeFood(df)

    # Create the bar plot
    fig2, ax2 = plt.subplots()
    df2.plot(kind='bar', ax=ax2, color=['brown', 'blue', 'green', 'red', 'pink', 'yellow'])
    ax2.set_title("Food Type vs Family Type")
    ax2.set_xlabel("Family Type")
    ax2.set_ylabel("Food Type Spending")
    st.pyplot(fig2) 




st.write("____")
col1 , col2 , col3 = st.columns([1 ,8, 1])   
with col2:
    st.markdown("#### Which product category generates the highest revenue and what's the distribution of spending across categories?")

col1 , col2 , col3 = st.columns([1,3, 1])   

with col2:
    df1 = functions.eduVscampaign(df)
    fig , ax = plt.subplots()
    df1.plot(kind='bar' ,ax = ax)
    st.pyplot(fig)



st.write("____")
col1 , col2 , col3 = st.columns([1 ,8, 1])   
with col2:
    st.markdown("####  Is there a correlation between different product categories (e.g., do wine buyers also buy more meat)?")

col1 , col2 , col3 = st.columns([1,3, 1])   

with col2:
    fig , ax = plt.subplots()
    sns.heatmap(df[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].corr(), annot = True , linecolor="yellow" , linewidths = 2)
    st.pyplot(fig)



st.write("____")
col1 , col2 , col3 = st.columns([2 ,8, 1])   
with col2:
    st.markdown("####   What's the average basket size (total spend) per customer and its distribution?")

col1 , col2 , col3 = st.columns([1,3, 1])   

with col2:
    fig , ax = plt.subplots()
    sns.histplot(df['Total_Spending']/6 , kde=True)
    st.pyplot(fig)



st.write("____")
col1 , col2 , col3 = st.columns([2 ,8, 1])   
with col2:
    st.markdown("####   What's the preferred shopping channel (web/catalog/store) among different customer segments?")

col1 , col2 , col3 = st.columns(3)   

with col1:
    df1 = functions.famVsshp(df)
    fig1 , ax1 = plt.subplots()
    df1.plot(kind='bar' ,ax = ax1)
    st.pyplot(fig1)
with col2:
    df1 = functions.eduVsshp(df)
    fig1 , ax2 = plt.subplots()
    df1.plot(kind='bar' ,ax = ax2)
    st.pyplot(fig1)
with col3:
    df1 = functions.marVsshp(df)
    fig1 , ax3 = plt.subplots()
    df1.plot(kind='bar' ,ax = ax3)
    st.pyplot(fig1)







