import pandas as pd 

class YahooCSV:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = None
        self._process()

    def _process(self):
        self.df = pd.read_csv(file_path) 

    def get_data(self):
        pass
