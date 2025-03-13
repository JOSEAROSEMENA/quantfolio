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

                ax.legend()
                st.pyplot(fig)
            else:
                st.error(f"No data found for {ticker}")
        
        except Exception as e:
            st.error(f"Error fetching data: {e}")