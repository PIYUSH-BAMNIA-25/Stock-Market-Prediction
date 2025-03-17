# 📈 **Stock Market Prediction Using Deep Learning**

## 📝 **Overview**
Stock market prediction is a crucial financial analysis task that helps investors make informed decisions. In this project, we use **deep learning (LSTM)** to predict future stock price trends based on historical data. The dataset contains stock price data, including Open, Close, High, Low prices, and various technical indicators like **SMA, EMA, RSI, and MACD**.

## 📚 **Libraries Used**
To carry out this project, several essential libraries are used:

- **Pandas** → Data manipulation and preprocessing.
- **NumPy** → Numerical operations and matrix handling.
- **Matplotlib & Seaborn** → Data visualization.
- **Scikit-learn** → Machine learning model training and evaluation.
- **TensorFlow/Keras** → Building and training deep learning models (LSTM).

## 🌍 **Data Source & Features**
The dataset is sourced from **KAGGLE** using CSV file. The dataset consists of:

- **Open price** → The price at market open.
- **Close price** → The price at market close.
- **High & Low prices** → The highest and lowest price of the stock on a given day.
- **Volume** → The number of shares traded in a day.
- **Technical Indicators** → Used for trend analysis and momentum prediction:
  - **SMA (Simple Moving Average) 10 & 50 Days**
  - **EMA (Exponential Moving Average) 10 & 50 Days**
  - **RSI (Relative Strength Index)**
  - **MACD (Moving Average Convergence Divergence)**

## 🔧 **Feature Engineering & Technical Indicators**
To improve the model’s predictive power, we compute the following indicators:

### **📊 1️⃣ Simple Moving Average (SMA)**
- SMA is used to smooth price data and identify trends.
- **Formula:**
  \[ SMA_n = \frac{\sum Price_{i}}{n} \]
  - Where \( n \) is the period (e.g., 10, 50 days).

### **📈 2️⃣ Exponential Moving Average (EMA)**
- EMA gives more weight to recent prices, making it more responsive to changes.
- **Formula:**
  \[ EMA = (Price \times Multiplier) + (Previous EMA \times (1 - Multiplier)) \]
  \[ Multiplier = \frac{2}{n+1} \]

### **📉 3️⃣ Relative Strength Index (RSI)**
- Measures stock momentum between gains and losses.
- Used to determine overbought/oversold conditions.
- **Formula:**
  \[ RSI = 100 - \left( \frac{100}{1 + RS} \right) \]
  \[ RS = \frac{Avg\ Gain}{Avg\ Loss} \]

### **🔄 4️⃣ Moving Average Convergence Divergence (MACD)**
- Identifies momentum changes and trends.
- **Formula:**
  \[ MACD = EMA_{12} - EMA_{26} \]
  - A Signal Line is derived from a **9-day EMA of MACD**.

## 🧠 **Deep Learning Models Used**
This project use one Deep Learning model:

### **🔮 2️⃣ LSTM (Long Short-Term Memory - Deep Learning)**
✅ Best suited for time-series forecasting.  
✅ Captures long-term dependencies in stock price trends.  
✅ Reduces vanishing gradient issues in deep networks.  

## 🔄 **Data Preprocessing Steps**
✔ **Handling Missing Values** → Remove NaN entries.  
✔ **Feature Scaling** → Normalize using MinMaxScaler.  
✔ **Train-Test Split** → Split into 80% training, 20% testing.  
✔ **Reshaping for LSTM** → Convert dataset into 3D array.  

## 📊 **Model Training & Evaluation**

### **LSTM Model Performance**
📌 Achieved an accuracy of **93%**.  
📌 Evaluated using **Loss & Accuracy Curves**.  
📌 Trained over **50 epochs** to achieve stability.  

## 📈 **Visualization & Insights**
✔ **Closing Price Trend** → Line plot showing stock price movement.  
✔ **SMA & EMA Comparisons** → Highlights bullish/bearish trends.  
✔ **RSI & MACD Indicators** → Helps identify buy/sell signals.  

## 🔚 **Conclusion & Future Enhancements**
🎯 This project successfully predicts stock price trends using **ML & DL models**.  
💡 Future improvements:
✔ **Incorporating News Sentiment Analysis** → To gauge market reactions.  
✔ **Hyperparameter Tuning** → Improve model accuracy.  
✔ **Adding more technical indicators** → Bollinger Bands, ADX.  
✔ **Deploying as a Web Application** → Using Flask/Django for real-time predictions.  

🚀 **This model serves as a strong foundation for stock market forecasting!**
