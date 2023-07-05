import pandas as pd
import yfinance as yf
from datetime import datetime, date, timedelta
import plotly.express as px
import plotly.graph_objects as go

# Getting stock data for the last 6 months
start_date = datetime.now() - pd.DateOffset(months=6)
end_date = datetime.now()
tickers = ['AAPL', 'MSFT', 'NFLX', 'GOOG']
df_list = []

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    df_list.append(data)

df = pd.concat(df_list, keys=tickers, names=['Ticker', 'Date'])

# Printing head of the concatenated DataFrame
print(df.head())

# Reset the index of the DataFrame
df = df.reset_index()
print(df.head())

# Creating a line plot for stock market performance
fig = px.line(df, x='Date', y='Close', color='Ticker', title="Stock Market Performance for the Last 6 Months")
fig.show()

# Creating an area plot for stock prices
fig = px.area(df, x='Date', y='Close', color='Ticker', facet_col='Ticker',
              labels={'Date': 'Date', 'Close': 'Closing Price', 'Ticker': 'Company'},
              title='Stock Prices for Apple, Microsoft, Netflix, and Google')
fig.show()

# Calculating moving averages
df['MA10'] = df.groupby('Ticker')['Close'].rolling(window=10).mean().reset_index(0, drop=True)
df['MA20'] = df.groupby('Ticker')['Close'].rolling(window=20).mean().reset_index(0, drop=True)

# moving averages for each ticker
for ticker, group in df.groupby('Ticker'):
    print(f'Moving Averages for {ticker}')
    print(group[['MA10', 'MA20']])

    # Creating a line plot for moving averages
    fig = px.line(group, x='Date', y=['Close', 'MA10', 'MA20'], title=f"{ticker} Moving Averages")
    fig.show()

# Calculating volatility
df['Volatility'] = df.groupby('Ticker')['Close'].pct_change().rolling(window=10).std().reset_index(0, drop=True)

# Creating a line plot for volatility
fig = px.line(df, x='Date', y='Volatility', color='Ticker', title='Volatility of All Companies')
fig.show()

# stock data for each company for the last six months and creating candlestick charts
today = date.today()
end_date = today.strftime("%Y-%m-%d")
start_date = (date.today() - timedelta(days=180)).strftime("%Y-%m-%d")

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    data["Date"] = data.index
    data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
    data.reset_index(drop=True, inplace=True)
    print(data.head())

    # Creating a candlestick chart
    figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"], high=data["High"],
                                            low=data["Low"], close=data["Close"])])
    figure.update_layout(title=f"{ticker} Stock Price Analysis", xaxis_rangeslider_visible=False)
    figure.show()

# Creating a line plot with rangeslider for Google
data = yf.download('GOOG', start=start_date, end=end_date, progress=False)
data["Date"] = data.index

# Creating a candlestick chart for Google
figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"], high=data["High"],
                                        low=data["Low"], close=data["Close"])])
figure.update_layout(title="Google Stock Price Analysis", xaxis_rangeslider_visible=False)
figure.show()

# Creating a line plot with rangeslider for Google
figure = px.line(data, x='Date', y='Close', title='Stock Market Analysis with Rangeslider')
figure.update_xaxes(rangeslider_visible=True)
figure.show()

# Creating a line plot with time period selectors for Google
figure = px.line(data, x='Date', y='Close', title='Stock Market Analysis with Time Period Selectors')
figure.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
figure.show()
