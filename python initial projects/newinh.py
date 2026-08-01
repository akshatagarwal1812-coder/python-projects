from abc import ABC, abstractmethod 
show_expected_result = True
show_hints = True
class Asset(ABC):
    def __init__(self,price):
        self.price=price
    @abstractmethod
    def get_description(self):
        pass
class Stock(Asset):
    def __init__(self,ticker,price,description):
        self.ticker=ticker
        super().__init__(price)
        self.description=description
    def get_description(self):
        return f"{self.ticker}: {self.description} -- ${self.price}"
class Bond(Asset):
    def __init__(self,bondprice,bondname,duration,interest):
        super().__init__(bondprice)
        self.bondname=bondname
        self.duration=duration
        self.interest=interest
    def get_description(self):
        return f"{self.bondname}: {self.duration} : ${self.price} : {self.interest}%"
ticker = "MSFT"
price = 400.00
description = "Microsoft Corporation"
bondname = "30 Year US Treasury"
bondprice = 100.00
duration = 30
interest = 4.38

# ******* DO NOT CHANGE THIS CODE ********
stock = Stock(ticker, price, description)
print(stock.get_description())

bond = Bond(bondprice, bondname, duration, interest)
print(bond.get_description())