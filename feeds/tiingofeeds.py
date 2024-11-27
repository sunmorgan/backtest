import pandas as pd 
import requests

class TiingoCSV:
    def __init__(self, api_key):
        self._api_key = api_key

    def get_data(self, symbol, start_date):
        self.headers = {
                'Content-Type': 'application/json'
                } 
        response = requests.get(f"https://api.tiingo.com/tiingo/daily/{symbol.lower()}/prices?startDate={start_date}&token={self._api_key}", headers=self.headers)
        print(response.json())
