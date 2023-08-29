import streamlit as st
import pandas as pd
import yfinance as yf
from PIL import Image

st.write('''# Simple Stock Price App TSLA''')


image = Image.open('teslaimage.jpg')
col1, col2 = st.columns(2)
with col1:
    st.write('''### Tesla Price and Volume''')
       
with col2:
    st.image(image)
    
stock ='TSLA'

# Create a ticker object
ticker = yf.Ticker(stock)

stock_data = ticker.history(period='2 months',start='2022-8-1',end='2023-8-1')
print(stock_data)

st.write('''### Closing Price''')
st.line_chart(stock_data.Close)
st.write('''### Volume''')
st.line_chart(stock_data.Volume)

