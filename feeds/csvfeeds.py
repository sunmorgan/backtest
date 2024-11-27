import pandas as pd

class CSVFeeds:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = None
        self._load_data()

    def _load_data(self):
        self._df = pd.read_csv(self.file_path)
        self._data = self._df.to_string() 

    def get_data(self):
        return self._data
