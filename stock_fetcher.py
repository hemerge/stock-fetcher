import yfinance as yf
import json
from datetime import datetime

class NSEStockFetcher:
    def __init__(self, symbols, circuit_percent=10):
        self.symbols = symbols
        self.circuit_percent = circuit_percent  # Default circuit limit (can be modified per stock)

    def fetch_stock_data(self, symbol):
        """ Fetch stock data from Yahoo Finance for a given symbol """
        stock = yf.Ticker(symbol + ".NS")  # NSE Stocks
        hist = stock.history(period="1d")

        if hist.empty:
            return None

        # Get previous close & last traded price
        previous_close = stock.info.get("previousClose", 0)
        last_traded_price = hist["Close"].values[-1] if len(hist) > 0 else previous_close
        
        # Get last traded timestamp
        last_traded_at = self.get_last_traded_timestamp(hist)

        # Compute Upper & Lower Circuits
        upper_circuit, lower_circuit = self.compute_circuit_limits(previous_close)

        return {
            "Name": stock.info.get("longName"),
            "Symbol": symbol,
            "Price Info": {
                "Open": hist["Open"].values[-1],
                "High": hist["High"].values[-1],
                "Low": hist["Low"].values[-1],
                "Close": last_traded_price,
                "Previous Close": previous_close,
                "Upper Circuit": upper_circuit,
                "Lower Circuit": lower_circuit,
                "Last Traded Price": last_traded_price,
                "Last Traded At": last_traded_at
            }
        }

    def get_last_traded_timestamp(self, hist):
        """ Extracts the last traded date and time from the history data """
        last_timestamp = hist.index[-1]  # Get last timestamp from history
        return last_timestamp.strftime("%Y-%m-%d %H:%M:%S")  # Format as "YYYY-MM-DD HH:MM:SS"

    def compute_circuit_limits(self, prev_close):
        """ Estimate upper and lower circuit limits based on the given circuit percentage """
        upper_circuit = prev_close * (1 + self.circuit_percent / 100)
        lower_circuit = prev_close * (1 - self.circuit_percent / 100)
        return round(upper_circuit, 2), round(lower_circuit, 2)

    def get_all_stocks_data(self):
        """ Fetch stock data for all symbols """
        stock_data_list = []

        for symbol in self.symbols:
            stock_data = self.fetch_stock_data(symbol)
            if stock_data:
                stock_data_list.append(stock_data)
        
        return stock_data_list


def main():
    # Initialize stock symbols
    symbols = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "SBIN"]

    # Create an instance of NSEStockFetcher
    fetcher = NSEStockFetcher(symbols)

    print("Fetching stock data...\n")
    stock_data_list = fetcher.get_all_stocks_data()

    if not stock_data_list:
        print("No data found!")
        return

    # Beautify JSON output
    beautified_json = json.dumps(stock_data_list, indent=4)
    print("\nBeautified JSON Output:\n")
    print(beautified_json)


if __name__ == "__main__":
    main()