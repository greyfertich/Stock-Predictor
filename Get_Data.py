import pandas_datareader.data as web

class GetData:
    def get_price(symbol, start, end):
        df = web.DataReader(symbol, 'quandl', start, end)
        df = df.drop('Open',1)
        df = df.drop('High',1)
        df = df.drop('Low',1)
        df = df.drop('Volume',1)
        df = df.drop('ExDividend',1)
        df = df.drop('SplitRatio',1)
        df = df.drop('AdjOpen',1)
        df = df.drop('AdjHigh',1)
        df = df.drop('AdjLow',1)
        df = df.drop('AdjClose',1)
        df = df.drop('AdjVolume',1)
        return df
