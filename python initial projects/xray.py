class xraygraphics:
    def my_decorater(func):
        def wrapper(*args, **kwargs):
            print("welcome to xray graphics")
            result = func(*args, **kwargs)
            print("thank you for visiting xray graphics")
            return result
        return wrapper
    def __init__(self, customer, balance):
        self.customer = customer
        self.balance = balance
    @my_decorater
    def details(self):
        print(f"Customer: {self.customer}, Balance: {self.balance}")    
a=xraygraphics("MR.ashish", 62541)
b=xraygraphics("MR.romi", 12000)    
c=xraygraphics("MR.tandon", 82541)
inp=input("Enter the customer name: ")
if inp=="MR.ashish":
    a.details() 
if inp=="MR.romi":
    b.details() 
if inp=="MR.tandon":
    c.details()