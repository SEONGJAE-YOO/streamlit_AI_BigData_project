import imp
import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
# Simple Stock Price App (2000-01-01 ~ 2022-01-28)
Shown are the stock **closing price** and ***volume*** of Google!

""")

#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2000-01-01', end='2022-01-28')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
# Copyright 2022. SeongJae Yu all rights reserved. (유성재 포토폴리오)
""")