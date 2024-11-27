from feeds.tiingofeeds import TiingoCSV

def main():
   tiingo_api_key = None
   tingo_feed = TiingoCSV(tiingo_api_key)

   data = tingo_feed.get_data("aapl", "2022-01-01")


if __name__ == "__main__":
    main()
