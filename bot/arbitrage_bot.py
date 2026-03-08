import time
import json
import requests

class ArbitrageBot:
    def __init__(self):
        self.markets = []
        self.flash_loan_provider = "YOUR_FLASH_LOAN_PROVIDER"

    def scan_prices(self):
        while True:
            for market in self.markets:
                price = self.get_price(market)
                print(f"Price at {market}: {price}")
            time.sleep(10)  # Scan every 10 seconds

    def get_price(self, market):
        response = requests.get(market)
        data = response.json()
        return data['price']  # Assuming the response contains a price field

    def execute_flash_loan(self, amount):
        # Logic to execute flash loan transaction
        print(f"Executing flash loan of {amount}")
        # Add appropriate code to interact with your blockchain here.

    def add_market(self, market):
        self.markets.append(market)

if __name__ == '__main__':
    bot = ArbitrageBot()
    bot.add_market("https://api.example.com/market1")
    bot.add_market("https://api.example.com/market2")
    bot.scan_prices()