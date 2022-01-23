import yfinance as yf


class GetStockData:
    def __init__(self):
        return

    def get_data(self, ticker):
        data = yf.Ticker(ticker).history(period='1y')[[
            'Close', 'Open', 'High', 'Volume', 'Low'
        ]]
        return data