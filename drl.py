import yfinance as yf
import pandas as pd

stock_list = ["SPY","BND","QQQ","VNQ","IWM","VIG","BIL"]

df = pd.DataFrame()
for s in stock_list:
    stock = yf.Ticker(s)
    # tmp_df = stock.dividends
    # tmp_df = tmp_df.reset_index()
    # tmp_df = tmp_df.rename(columns = {'Dividends':s,'index':'Date'})
    # df = pd.concat([df,tmp_df])

