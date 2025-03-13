# 📈 Stock Price Prediction and Portfolio Optimization Tool  
This project is a **Streamlit-based web app** that allows users to:  
✅ Fetch real-time stock price data using `yfinance`  
✅ Visualize historical stock prices with dynamically adjusted x-axis spacing  
✅ Predict future stock prices using a **Linear Regression model**  
✅ Display key model performance metrics like **Mean Squared Error (MSE)** and **R² Score**  

---

## 🚀 Features  
### ✅ **Real-Time Data Fetching**  
- Uses the `yfinance` library to pull stock price data for any publicly traded stock.  
- User inputs ticker symbol and date range (start and end dates).  

---

### ✅ **Dynamic Plotting**  
- Uses `matplotlib` to plot historical stock prices.  
- Dynamic x-axis formatting based on the date range:  
  - **< 1 year** → Monthly intervals  
  - **1–5 years** → Quarterly intervals  
  - **> 5 years** → Yearly intervals  

---

### ✅ **Performance Metrics**  
- Displays:  
  - **Mean Squared Error (MSE)** – Measures average squared prediction error  
  - **R² Score** – Measures how well the model fits the data  

---

## 🏗️ Setup Instructions  
### **1. Clone the Repository**  
```bash
git clone https://github.com/JOSEAROSEMENA/quantfolio.git
cd quantfolio
```

### **2. Create a Virtual Environment **
```bash
python -m venv venv  
source venv/bin/activate  # MacOS/Linux  
# .\venv\Scripts\activate  # Windows  
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt  
```

### 4. Run the Streamlit App  
```bash
streamlit run app.py  
```