import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Banking Customer Analytics Project 
#Dataset Fields:

# Customer_ID
# Embassy
# RM_Name
# Account_Balance
# Monthly_Revenue
# Monthly_Cost
# Transaction_Count
# Account_Status

import pandas as pd

df = pd.read_csv("banking_data.csv")

print(df.head())

#Understand the Data
print(df.info())
print(df.describe())
# Check for Missing Values

print(df.isnull().sum())

# Create a Profit Column
df["Profit"] = df["Revenue"] - df["Cost"]

print(df.head())
# Calculate Key Business Metrics
print("Total Revenue:", df["Revenue"].sum())

print("Total Cost:", df["Cost"].sum())

print("Total Profit:", df["Profit"].sum())

# Analyze by Embassy

embassy_revenue = df.groupby("Embassy")["Revenue"].sum()
print(embassy_revenue)

# nalyze by RM_Name
rm_revenue = df.groupby("RM_Name")["Revenue"].sum()
print(rm_revenue)

# Find Top Customers
top_customers = df.nlargest(10, "Revenue")
print(top_customers.head(5))
embassy_revenue = df.groupby("Embassy")["Revenue"].sum()

print(embassy_revenue)

# Create Your First Chart
embassy_revenue.plot(kind="bar")
plt.title("Embassy Wise Revenue")
plt.xlabel("Embassy")
plt.ylabel("Revenue")
plt.show()