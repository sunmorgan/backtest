import pandas as pd 
import requests
import csv
import os

class TiingoCSV:
    def __init__(self, api_key):
        self._api_key = api_key
        self.dir = 'data'

        # in case this doesn't exist for some reason
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def get_data(self, symbol, start_date):
        self.headers = {
                'Content-Type': 'application/json'
                } 
        
        api = f"https://api.tiingo.com/tiingo/daily/{symbol.lower()}/prices?startDate={start_date}&token={self._api_key}"
        response = requests.get(api, headers=self.headers).json()
        csv_name = os.path.join(self.dir, f"tiingo-{symbol}-{start_date}.csv")

        with open(csv_name, 'w', newline='') as csvfile:
            fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume', 'adjOpen', 'adjHigh', 'adjLow',
                          'adjClose', 'adjVolume', 'dividend', 'split']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for r in response:
                date = r['date'] 
                openn = r['open']
                high = r['high']
                low = r['low']
                close = r['close']
                volume = r['volume']
                adj_open = r['adjOpen']
                adj_high = r['adjHigh']
                adj_low = r['adjLow']
                adj_close = r['adjClose']
                adj_volume = r['adjVolume']
                dividend = r['divCash']
                split = r['splitFactor']

                writer.writerow({'date': date, 'open': openn, 'high': high, 'low': low,
                                 'close': close, 'volume': volume, 'adjOpen': adj_open, 'adjHigh': adj_high,
                                 'adjLow': adj_low, 'adjVolume': adj_volume, 'dividend': dividend, 'split': split})
