import pandas as pd
import numpy as np
from datetime import datetime
from plotly.offline import plot
import plotly.graph_objs as go
import os
import coinbase

class graph():
	
    DATA_PATH = os.getcwd() + '\data\coinbase\historic_rates\\'
    CANDLES = []
    TIME_DATA = []
    LOW_DATA = []
    HIGH_DATA = []
    OPEN_DATA = []
    CLOSE_DATA = []
    VOLUME_DATA = []
    EMA12 = []
    EMA26 = []
    MACD = []
    SIGNAL = []
    
    def __init__(self, trading_pair):
        global CANDLES
        
        api = coinbase.api()
        self.CANDLES = api.historic_rates(trading_pair)
        
    def ema12(self, values):
        values = np.array(values)
        return pd.ewm(values, span=12)[-1]
        
    def candle_graph(self):
                        
        fig = go.Figure(data=[go.Candlestick(x=self.TIME_DATA, open=self.OPEN_DATA, high=self.HIGH_DATA, low=self.LOW_DATA, close=self.CLOSE_DATA)])
        
        plot(fig)
    
        
    def parse_data(self):
        for candle in self.CANDLES:
            self.TIME_DATA.append(datetime.utcfromtimestamp(int(candle[0])).strftime('%Y-%m-%d %H:%M:%S'))
            self.LOW_DATA.append(candle[1])
            self.HIGH_DATA.append(candle[2])
            self.OPEN_DATA.append(candle[3])
            self.CLOSE_DATA.append(candle[4])
            self.VOLUME_DATA.append(candle[5])
            self.EMA12.append(self.ema12(self.CLOSE_DATA))
            
        print(self.EMA12)

    def write_csv(self):
        index = 0
        list_keys = ['time', 'low', 'high', 'open', 'close', 'volume']
        candles = []
        candle = {}

        for interval in self.CANDLES:
            candle = dict(zip(list_keys, interval))
            candles.append(candle)
                
        data_frame = pd.DataFrame(data=candles)
        data_frame.to_csv('data.csv')
        print('Data written to file')
        
if __name__ == '__main__':
    graph = graph('BTC-USD')
    graph.parse_data()
'''
    'time' bucket start time
    'low' lowest price during the bucket interval
    'high' highest price during the bucket interval
    'open' opening price (first trade) in the bucket interval
    'close' closing price (last trade) in the bucket interval
    'volume' volume of trading activity during the bucket interval
'''