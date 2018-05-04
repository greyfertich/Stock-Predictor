import pandas_datareader.data as web

class get_Data:
    def get_price(symbol, start, end):
        df = web.DataReader(symbol, 'iex', start, end)
        df = df.drop('open',1)
        df = df.drop('high',1)
        df = df.drop('low',1)
        df = df.drop('volume',1)
        return df
