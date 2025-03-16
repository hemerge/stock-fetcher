import requests
import json
import time

def fetch_nse_stock_data(symbols):
    url_template = "https://www.nseindia.com/api/quote-equity?symbol={}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.nseindia.com/market-data/live-equity-market",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive"
    }

    # Create a session to manage cookies
    session = requests.Session()

    # Fetch the home page to get initial cookies
    print("🔄 Initializing session with NSE...")
    session.get("https://www.nseindia.com", headers=headers)
    time.sleep(2)  # Give time to avoid blocking

    stock_data_list = []

    for symbol in symbols:
        print(f"📥 Fetching data for {symbol}...")

        try:
            response = session.get(url_template.format(symbol), headers=headers)

            # If response is empty or invalid, print an error
            if response.status_code != 200 or response.text.strip() == "":
                print(f"❌ Error fetching {symbol}: HTTP {response.status_code}, Empty response")
                continue

            stock_data = response.json()  # Convert to JSON

            # Extract required details
            stock_info = {
                "Name": stock_data.get("info", {}).get("companyName"),
                "Symbol": stock_data.get("info", {}).get("symbol"),
                "Price Info": {
                    "Open": stock_data.get("priceInfo", {}).get("open"),
                    "High": stock_data.get("priceInfo", {}).get("dayHigh"),
                    "Low": stock_data.get("priceInfo", {}).get("dayLow"),
                    "Close": stock_data.get("priceInfo", {}).get("lastPrice"),
                    "Previous Close": stock_data.get("priceInfo", {}).get("previousClose"),
                }
            }

            stock_data_list.append(stock_info)

        except json.JSONDecodeError:
            print(f"❌ Error: Could not decode JSON for {symbol}. Response might be blocked.")
        except Exception as e:
            print(f"❌ Error fetching {symbol}: {str(e)}")

        time.sleep(2)  # Delay to prevent blocking

    # Beautify JSON output
    beautified_json = json.dumps(stock_data_list, indent=4)
    print("\n📜 Beautified JSON Output:\n")
    print(beautified_json)

    return stock_data_list

# Example: Fetch data for multiple NSE stocks
symbols = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "SBIN"]
fetch_nse_stock_data(symbols)