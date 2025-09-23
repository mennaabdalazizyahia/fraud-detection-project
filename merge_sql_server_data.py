import pyodbc
print(pyodbc.drivers()) 
import pandas as pd 
import numpy as np 

server = r'DESKTOP-29SNGGH'   
database = 'INSTANT'
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

conn = pyodbc.connect(conn_str)

df_users = pd.read_sql("SELECT * FROM dbo.users_data", conn)
df_users
df_cards = pd.read_sql("SELECT * FROM dbo.cards_data", conn)
df_cards
df_transactions = pd.read_sql("SELECT TOP 1000 * FROM transactions_data", conn)
df_transactions

import json
with open ('C:\\Users\\Menna\\Downloads\\archive\\mcc_codes.json','r') as file:
    df_mcc = json.load(file)
print(json.dumps(df_mcc,indent=4))
df_mcc = pd.DataFrame(list(df_mcc.items()), columns= ['mcc' , 'Details'])
df_mcc

import json
with open ('C:\\Users\\Menna\\Downloads\\archive\\train_fraud_labels.json','r') as file:
    fraud = json.load(file)
print(json.dumps(fraud,indent=4))
df_fraud = pd.DataFrame(list(fraud["target"].items()), columns=["transaction_id", "Is_fraud"])


df_transactions["transaction_id"] = pd.to_numeric(df_transactions["transaction_id"], errors="coerce").astype("Int64")
df_transactions["client_id"] = pd.to_numeric(df_transactions["client_id"], errors="coerce").astype("Int64")
df_transactions["card_id"] = pd.to_numeric(df_transactions["card_id"], errors="coerce").astype("Int64")
df_transactions["mcc"] = df_transactions["mcc"].astype(str)
df_users["id"] = pd.to_numeric(df_users["id"], errors="coerce").astype("Int64")
df_cards["id"] = pd.to_numeric(df_cards["id"], errors="coerce").astype("Int64")
df_cards["client_id"] = pd.to_numeric(df_cards["client_id"], errors="coerce").astype("Int64")
df_fraud["transaction_id"] = pd.to_numeric(df_fraud["transaction_id"], errors="coerce").astype("Int64")
df_mcc["mcc"] = df_mcc["mcc"].astype(str)



df_merged = df_transactions.merge(df_users, left_on="client_id", right_on="id", how="left", suffixes=("", "_user"))
df_merged = df_merged.merge(df_cards, left_on="card_id", right_on="id", how="left", suffixes=("", "_card"))
df_merged = df_merged.merge(df_fraud, on="transaction_id", how="left")
df_merged = df_merged.merge(df_mcc, on="mcc", how="left")


print("Final shape:")
df_merged.head(3)

df_merged.to_csv("merged_dataset.csv")
