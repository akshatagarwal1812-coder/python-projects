a=input("enter a number between 5 and 9")
c=int(a)
if(c<5 or c>9):
    raise ValueError("number must be between 5 and 9")
elif(a=="qite"):
    print("unwanted input")
