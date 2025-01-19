# 📈 **Stock Market Prediction**

## 📝 **Overview**
The goal of this project is to predict future stock prices using historical stock market data. By leveraging machine learning techniques and various data processing tools, this model aims to forecast stock price movements based on different technical indicators. For this example, Google stock data has been used, but the approach can be adapted to other stocks as well.

## 📚 **Libraries Used**
To carry out this project, several important libraries have been used:

- **Pandas**: Data manipulation and analysis tool.
- **NumPy**: For handling large, multi-dimensional arrays and matrices.
- **Matplotlib** & **Seaborn**: Libraries for data visualization to generate charts and plots.
- **Scikit-learn**: A machine learning library for data preprocessing, model building, and evaluation.

## 🌍 **Data Source**
The dataset for this project is sourced from Yahoo Finance using the **yfinance** library. The data represents historical stock prices for Google (GOOG) from August 2004 to the current date. The dataset includes the following stock metrics:

- **Open price**
- **Close price**
- **High and Low prices**
- **Volume of stock traded**

The dataset is cleaned and processed to remove irrelevant or missing data points. It is then used to compute features like the **daily price change**.

## 🔧 **Feature Engineering**
Feature engineering is a crucial step in predicting stock prices. In this project, the **daily price change** is calculated using the following formula:

## **Daily Price Change= ( Close - Open )/open *100**


This feature captures daily volatility and helps the model understand price trends.

## 🧠 **Machine Learning Models**
Various machine learning algorithms are employed to predict stock prices:

1. **Support Vector Machine (SVM)**: A classification algorithm used for regression tasks in stock prediction. SVM finds the best hyperplane that separates data points.
2. **Grid Search**: Used for hyperparameter tuning to enhance model performance.
3. **Cross-Validation**: Helps evaluate the model’s ability to generalize to new data.

## 🔄 **Data Preprocessing**
Data preprocessing steps include:

- **Normalization**: Scaling numerical features to a uniform range, ensuring that no single feature dominates the model.
- **Train-Test Split**: Dividing data into training and testing sets to assess the model’s performance.
- **Rescaling**: Using techniques like **MinMaxScaler** to make sure the model learns efficiently.

## 📊 **Model Evaluation**
The model’s performance is evaluated using the following metrics:

- **Accuracy score**: Measures how well the model predicts stock price trends.
- **Confusion Matrix**: Provides insight into the classification performance.
- **Cross-Validation**: Used to assess how well the model generalizes.

## 📉 **Visualization**
Visualizing the results is a key part of understanding stock data and the model’s predictions:

- **Candlestick charts**: Show price movements in a graphical format, helping analyze market behavior.
- **Line plots**: Display the closing price over time to visualize trends.

  
## 🔚 **Conclusion**
This project demonstrates the use of machine learning models to predict future stock prices based on historical data. While stock market prediction is inherently challenging due to the multitude of influencing factors, this project provides a strong foundation for further refinement. The model can be expanded to predict other stocks or include additional features, such as news sentiment or macroeconomic indicators.
