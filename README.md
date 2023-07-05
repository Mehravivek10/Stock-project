In this project, we present a summary of our stock market analysis using python. Our goal 
was to analyse and understand the behaviour of various stocks in order to make informed 
investment decisions. To achieve this, we utilized python’s powerful libraries such as pandas, 
NumPy and yfinance. Stock market Performance Analysis involves calculating moving 
averages, measuring volatility, conducting correlation analysis and analysing various aspects 
of the stock market to gain a deeper understanding of the factors that affect stock prices and 
the relationships between the stock prices of different companies.
The first step of our analysis involved collecting historical stock data from reliable sources. 
We obtained the data through APIs. We then imported the data into python using Pandas, 
allowing us to manipulate and analyse the data effectively.
Next, we perform various data analysis and visualization tasks on stock data. It starts by 
retrieving the stock prices for the last 6 months for four companies: Apple (AAPL), 
Microsoft (MSFT), Netflix (NFLX), and Google (GOOG). The data is downloaded using the 
‘yfinance’ library and stored in a Pandas DataFrame.
The code then proceeds to visualize the stock market performance using line and area plots, 
showing the closing prices of the companies over time. Moving averages are calculated for 
each company and displayed in a line plot to identity trends and pattern. The volatility of the 
companies’ stock prices is also calculated and plotted to assess the level of risk.
Next, the code retrieves the stock prices for the past 6 months for google specifically and 
creates a candlesticks chart, which displays the opening, high, low, and closing prices for 
each day. The candlestick chart provides a visual representation of price fluctuations. The 
same process is repeated for the other three companies, generating individual candlestick 
charts for each.
Additionally, the code includes line plots with a rangeslider and time period selectors 
specifically for Google’s stock prices. These interactive visualizations allow users to explore 
the stock market data by selecting a specific time period or adjusting the range of the plot.
In summary, this code retrieves and analyses stock market data, visualizes the stock prices 
using various plots, calculates moving averages and volatility, and generates candlesticks’ 
charts for each company’s stock prices. These visualizations help understand the 
performance, trends, and volatility of the stock market for the selected companies.
Conclusion:
The stock market analysis using python project offers a comprehensive analysis 
and visualization of stock market data for four companies: Apple (AAPL), 
Microsoft (MSFT), Netflix (NFLX), and Google (GOOG). By leveraging the ‘yfinance’
library and Pandas DataFrame, the code retrieves historical stock prices for the last 6 months 
and calculates moving averages and volatility to gain insights into market trends and risk 
levels. The visualizations, including line plots, area plots, and candlesticks’ charts, provide a 
clear representation of the stock market performance and price fluctuations over time. The 
inclusion of interactive features such as rangeslider and time period selectors enhance the 
user experience and allows for a more in-depth exploration of the data. Overall, this code 
serves as a valuable tool for analysing and understanding the stock market dynamics of the 
selected companies
