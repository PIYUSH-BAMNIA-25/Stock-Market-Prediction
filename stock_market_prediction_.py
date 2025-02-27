# -*- coding: utf-8 -*-
"""Stock Market Prediction .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LlNe2mMu3uYjU8lQNAKry70hR-fug0LJ

##***Stock Market Prediction***

###***Use a dataset of stock market data and build a model that can predict future stock prices***

***Importing all libraries which was important for this task***
"""

# first we import all libraries which was important for this task
!pip install mplfinance
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

pip install yfinance --upgrade --no-cache-dir

import yfinance as yf

# Get today's date
today = datetime.today().strftime('%Y-%m-%d')

# Download Google stock data up to today
df = yf.download("GOOG", start="2004-08-19", end=today)

df.rename(columns={'Price Ticker Date': 'Date'}, inplace=True)
print(df.head())

"""***Printing the Table :-***"""

print(df.head(10))

"""####*Get the info about Data :-*"""

df.info()

df['Daily Price change'] = (df['Close'] - df['Open'])/df['Open']*100
print(df.head(10))

df['daily high-low change'] = df['High'] - df['Open']
print(df.head(10))

df['target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)
print(df.head(10))

"""##***Ploting Some Graph of Data to Find The pattern:-***"""

# Closing Price Trend
plt.figure(figsize=(12, 6))
plt.plot(df['Close'])
plt.title('Google Stock Closing Price Trend')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()

# Daily Price Change Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Daily Price change'], kde=True)
plt.title('Distribution of Daily Price Change')
plt.xlabel('Daily Price Change (%)')
plt.ylabel('Frequency')
plt.show()

#Relationship between Daily Price Change and Volume
plt.figure(figsize=(10, 6))
plt.scatter(df['Daily Price change'], df['Volume'], alpha=0.5)
plt.title('Daily Price Change vs. Volume')
plt.xlabel('Daily Price Change (%)')
plt.ylabel('Volume')
plt.show()

# Heatmap of Correlation
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

"""###***Training The Dataset :-***"""

#Make a training dataset
Data= df[["Close" ,"Open", "High" , "Low" , "Daily Price change", "daily high-low change" ,"target"]]

#Separating The Feature and Target Variable
X = Data[["Close" ,"Open", "High" , "Low" , "Daily Price change", "daily high-low change" ]]  # Features
y = Data["target"]  # Target variable

# Now you can split the data:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#standardizing the Data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Normalizing Data
scaler = MinMaxScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

"""##***Fitting Data into Model***

"""

# Initialize the SVM classifier
model = svm.SVC(kernel='rbf', C=1, gamma='scale')

# Train the model on standardized data
model.fit(X_train_scaled, y_train)

# Predict on test data
y_pred = model.predict(X_test_scaled)

"""###**Finding accuracy Of the model**"""

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='accuracy')
print(f"Cross-validated accuracy: {scores.mean() * 100:.2f}%")

"""####***Example User Data :-***"""

#This data is a Example User Data
user_data = {
    'Close': 197.12,
    'Volume': 24107300,
    'Open': 198.53,
    'High': 202.88,
    'Low': 196.69,
    'Daily Price change' : -0.71022,
    'daily high-low change' : 6.19
}

"""####***Converting User data into a dataframe :-***"""

#Converting User data into a dataframe
user_data_df = pd.DataFrame([user_data])

"""####***check that the dataframe was created or now:-***"""

#Checking that the dataframe is created successfully or not

print(user_data_df)

"""####***Predicting the Value:-***"""

#Predicting the Value
user_pred = model.predict(user_data_df[["Close" ,"Open", "High" , "Low" , "Daily Price change", "daily high-low change"]])

if user_pred[0] == 1:
    print("The stock price will go High")
else:
    print("The stock price will go Low")
