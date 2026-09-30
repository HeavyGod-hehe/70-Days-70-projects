import pandas as pd
from ai_service import analyize_Data

df = pd.read_csv("data.csv")
# print (df)
# print(df.head())
# df.info()
# print(df.describe())
# print(df.isnull().sum())
sales_region = (df.groupby("Region")["Sales"].mean())
total_sales = (df.groupby("Product")["Sales"].sum())
# print(df.groupby("Region")["Sales"].mean().sort_values(ascending=False))

summary = f"""
DataSet has {len(df)} rows

overAll Sales Stats: 
{df['Sales'].describe()}

average Sales By region:
{sales_region}

Total Sales by Product:
{total_sales}



"""


# print (summary)d

question = input("Whats Your Question? :  ")
answer = analyize_Data(summary,question)
print(answer)