# NSE Stock Data Fetcher

This script fetches stock data from Yahoo Finance for multiple NSE-listed stocks and provides details such as:
- **Name**
- **Symbol**
- **Open, High, Low, Close**
- **Previous Close**
- **Upper and Lower Circuit Limits**
- **Last Traded Price**
- **Last Traded At (Date & Time)**

## Prerequisites
Ensure you have Python 3 installed on your system. You can check your Python version by running:

```sh
python --version
```

## Installation

1. **Create and activate a virtual environment (optional but recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

2. **Install required dependencies:**

   ```sh
   pip install yfinance
   ```

## Configuration

The script fetches data for a predefined list of stock symbols. You can modify the stock list in `main()`:

```python
symbols = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "SBIN"]
```

The **circuit limit percentage** is set to **10%** by default but can be changed in the `NSEStockFetcher` constructor:

```python
fetcher = NSEStockFetcher(symbols, circuit_percent=10)
```

## Running the Script

Execute the script using:

```sh
python stock_fetcher.py
```

## Expected Output

A beautified JSON output with stock details will be displayed:

```json
[
    {
        "Name": "Reliance Industries Ltd",
        "Symbol": "RELIANCE",
        "Price Info": {
            "Open": 2301.50,
            "High": 2350.75,
            "Low": 2298.00,
            "Close": 2345.25,
            "Previous Close": 2312.90,
            "Upper Circuit": 2544.19,
            "Lower Circuit": 2081.61,
            "Last Traded Price": 2345.25,
            "Last Traded At": "2025-03-13 15:30:00"
        }
    }
]
```

## Notes
- Data is fetched from Yahoo Finance and is subject to availability.
- Ensure you have an active internet connection while running the script.

## Troubleshooting

- **ModuleNotFoundError: No module named 'yfinance'**  
  Run `pip install yfinance` to install the missing dependency.

- **No data found!**  
  Check if the stock symbol is correct and exists on Yahoo Finance.

## License
This project is open-source and free to use.


