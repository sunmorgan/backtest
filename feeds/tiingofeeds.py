import pandas as pd 
import requests
import csv 

class TiingoCSV:
    def __init__(self, api_key):
        self._api_key = api_key

    def get_data(self, symbol, start_date):
        self.headers = {
                'Content-Type': 'application/json'
                } 
        response = requests.get(f"https://api.tiingo.com/tiingo/daily/{symbol.lower()}/prices?startDate={start_date}&token={self._api_key}", headers=self.headers)
        csv_name = f"{symbol}-{start_date}"
        
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
