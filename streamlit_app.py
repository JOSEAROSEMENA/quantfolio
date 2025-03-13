import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

                # Rotate and format x-axis labels
                locator = mdates.MonthLocator(interval=3)
                formatter = mdates.ConciseDateFormatter(locator)
                ax.xaxis.set_major_locator(locator)
                ax.xaxis.set_major_formatter(formatter)
                plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

                ax.legend()
                st.pyplot(fig)

            else:
                st.error(f"No data found for {ticker}")
        
        except Exception as e:
            st.error(f"Error fetching data: {e}")