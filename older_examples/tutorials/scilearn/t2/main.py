import pandas as pd
import numpy as np
import yfinance as yf
# import iexfinance
# from iexfinance.stocks import get_historical_data
from datetime import datetime, date
# from vars import TOKEN_IEX

# start date should be within 5 years of current date according to iex API we have used
# The more data we have, the better results we get!

startt = datetime(2016, 1, 1)
endd = date.today()

# use your token in place of token which you will get after signing up on IEX cloud
# Head over to https://iexcloud.io/ and sign-up to get your API token
# df = get_historical_data("AAPL", start=start, end=end, output_format="pandas", token=TOKEN_IEX)

aapl = yf.Ticker('aapl')
# data = aapl.history(start='2022-05-22', end='2022-07-22', interval='90m',)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

data = aapl.history(period="max")
df = pd.DataFrame(data)
print(df)

# print(df)
