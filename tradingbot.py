from lumibot.brokers import Alpaca #Broker
from lumibot.backtesting import YahooDataBacktesting #Framework
from lumibot.strategies.strategy import Strategy #Trading bot
from lumibot.traders import Trader #deployment
from datetime import datetime

API_KEY = "PKRGWTLLWNM1HBD3TFNI"
API_SECRET = "M8SyWEicQJ73EgqcruaAYbPaXeoVuEHezol3tyZw"
BASE_URL = "https://paper-api.alpaca.markets/v2"

ALPACA_CREDS = {
    "API_KEY":API_KEY,
    "API_SECRET":API_SECRET,
    "PAPER": True
}

class MLTrader(Strategy):
    def initialize(self, symbol:str="NVDA"):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None

    #every tick
    def on_trading_iteration(self):
        if self.last_trade == None:
            order = self.create_order(
                self.symbol,
                10,
                "buy",
                type="market"
            )
            self.submit_order(order)
            self.last_trade = "buy"

#backtest time range
start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)

broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='sgstrat', broker=broker, parameters={"symbol":"NVDA"})

strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={"symbol":"NVDA"}
)