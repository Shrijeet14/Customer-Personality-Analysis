import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns


# df = pd.read_csv('data\Cleaned_marketing_campaign.csv')
# df = df.drop('Unnamed: 0',axis=1)
def incomeComparator(Income):
    if (Income <= 35397.000000):
        return 'Low Income'
    elif (Income > 35397.000000 and Income < 52161.539133):
        return 'Below Average Income'
    elif (Income >= 52161.539133 and Income <= 68655.500000):
        return 'Above Average Income'
    else :
        return 'High Income'


def check_fam (Kidhome,Teenhome) :
  if(Teenhome > 0 and Kidhome > 0) :
    return 'Family with Teen and Kid'
  elif(Kidhome > 0) :
    return 'Family With Kid'
  elif(Teenhome > 0) :
    return 'Family with Teen'
  else :
    return 'Single'



def transform(df):
    df = df.drop('Unnamed: 0',axis=1)
    df['Total_Spending'] = df['MntWines'] +df['MntFishProducts'] +df['MntFishProducts'] +df['MntSweetProducts'] +df['MntGoldProds']

    #Age
    df['Year_Birth']= pd.to_datetime(df['Year_Birth'] , format='%Y').dt.year
    df['Age'] = 2014 - df['Year_Birth']

    #Income Category
    df["Income_Category"] = df["Income"].apply(incomeComparator)

    #Campaign 
    df['Accepted_Campaign'] = df['AcceptedCmp1'] + df['AcceptedCmp2'] + df['AcceptedCmp3'] + df['AcceptedCmp4'] + df['AcceptedCmp5'] + df['Response']

    # family Status
    df['Family_Status'] = df.apply(lambda x: check_fam(x['Kidhome'], x['Teenhome']), axis=1)


    return df



def ageDist(df):
    return df['Age'] 


def TotalSpendingDist(df):
    return df['Total_Spending'] 

def maritalStatusTotalSpening(df):
    return df.groupby('Marital_Status')['Total_Spending'].sum()

def incomeWIseSpending(df):
    return df.groupby('Income_Category')[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum()


def expenVsincomeVsprod(df , category):
    df_income = df.groupby('Income_Category')[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum()
    df_income['Income_Category'] = df_income.index
    return df_income[df_income['Income_Category'] == category][['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].to_numpy().tolist()[0]


def eduVscampaign(df):
    return df.groupby('Education')['Accepted_Campaign'].sum()



def famVsTotalSpending(df):
   return df.groupby('Family_Status')['Total_Spending'].sum()


def famVsTypeFood(df):
   return df.groupby('Family_Status')[['MntWines', 'MntFruits',
       'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
       'MntGoldProds']].mean()


def revVsCat(df):
   return df[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum()

def famVsshp(df):
   return df.groupby('Family_Status')[['NumWebPurchases','NumCatalogPurchases', 'NumStorePurchases']].mean()

def marVsshp(df):
   return df.groupby('Marital_Status')[['NumWebPurchases','NumCatalogPurchases', 'NumStorePurchases']].mean()

def eduVsshp(df):
   return df.groupby('Education')[['NumWebPurchases','NumCatalogPurchases', 'NumStorePurchases']].mean()