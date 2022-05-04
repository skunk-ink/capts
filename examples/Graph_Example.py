import plotly.graph_objects as go
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
from plotly.subplots import make_subplots


start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 1, 1)
df = web.DataReader("MSFT", 'yahoo', start, end)
df.reset_index(inplace=True)
# moving average
exp12 = df['Close'].ewm(span=12, adjust=False).mean()
exp26 = df['Close'].ewm(span=26, adjust=False).mean()
macd = exp12 - exp26
signal = macd.ewm(span=9, adjust=False).mean()

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
                             yaxis='y1', name='Cnadlestick'))

fig.add_trace(go.Scatter(x=df['Date'], y=exp12, name='Moving Avg 12',
                        line=dict(color='royalblue',width=2)))

fig.add_trace(go.Scatter(x=df['Date'], y=exp26, name='Moving Avg 26',
                        line=dict(color='firebrick',width=2)))

fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'], yaxis='y2', name='Volume'))

# Add figure title
fig.update_layout(
    width=1100,
    height=600,
    title_text="Microsoft Stock",
    yaxis_tickformat='M'
)

fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))

# Set x-axis title
fig.update_xaxes(title_text="Date")

# Set y-axes titles
fig.update_yaxes(title_text="<b>primary</b> Close", secondary_y=False)
fig.update_yaxes(title_text="<b>secondary</b> Volume", range=[0, 300000000], secondary_y=True)

fig.show()