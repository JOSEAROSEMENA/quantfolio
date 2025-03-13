import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

st.title(" 📈 Quantfolio")


# User Input for Ticker Symbol
ticker = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL):", "AAPL")

#Date Range Input
start_date = st.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2025-01-01"))

# Fetch Stock Data
if st.button("Get Stock Data"):
    with st.spinner("Fetching data..."):
        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            if not data.empty:
                st.success(f"Data fetched successfully for {ticker}")
                
                # Display raw data
                st.subheader("Raw Data")
                st.write(data.tail())

                # Plot Closing Price
                st.subheader("Closing Price")
                fig, ax = plt.subplots()
                ax.plot(data.index, data["Close"], label="Closing Price", color="blue")
                ax.set_xlabel("Date")
                ax.set_ylabel("Price ($)")

                # 📅 Dynamic x-axis spacing based on date range
                date_diff = (end_date - start_date).days
                if date_diff <= 365:  # Less than 1 year → Monthly labels
                    locator = mdates.MonthLocator(interval=1)
                    formatter = mdates.DateFormatter('%b %Y')  # e.g., Jan 2023
                elif date_diff <= 5 * 365:  # 1–5 years → Quarterly labels
                    locator = mdates.MonthLocator(interval=3)
                    formatter = mdates.DateFormatter('%b %Y')
                else:  # More than 5 years → Yearly labels
                    locator = mdates.YearLocator()
                    formatter = mdates.DateFormatter('%Y')

                ax.xaxis.set_major_locator(locator)
                ax.xaxis.set_major_formatter(formatter)
                plt.xticks(rotation=45)
                # ✅ Prepare data for prediction
                data['Date_Ordinal'] = data.index.map(pd.Timestamp.toordinal)
                X = data[['Date_Ordinal']]
                y = data['Close']

                # Split data into train and test sets
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

                # ✅ Train Linear Regression Model
                model = LinearRegression()
                model.fit(X_train, y_train)

                # ✅ Predict on test set
                y_pred = model.predict(X_test)

                # ✅ Predict future values (30 days ahead)
                future_dates = pd.date_range(start=data.index[-1], periods=30, freq='B')  # Business days only
                future_ordinal = future_dates.map(pd.Timestamp.toordinal).values.reshape(-1, 1)
                future_predictions = model.predict(future_ordinal)

                # ✅ Plot Predictions
                ax.plot(data.index[-len(y_test):], y_pred, label="Predicted (Test)", color="orange", linestyle="--")
                ax.plot(future_dates, future_predictions, label="Future Prediction", color="red", linestyle="--")

                # ✅ Show Model Performance
                mse = mean_squared_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)
                st.write(f"**Mean Squared Error:** {mse:.2f}")
                st.write(f"**R² Score:** {r2:.2f}")
                ax.legend()
                st.pyplot(fig)
            else:
                st.error(f"No data found for {ticker}")
        
        except Exception as e:
            st.error(f"Error fetching data: {e}")