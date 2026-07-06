def decorator(func):
    def ak(*args, **kwargs):
        print("welcome to the library")
        result = func(*args, **kwargs)
        print("Thank you for using the library")
        return result
    return ak
class library:
    def __init__(self):
        self.books = []
        self.no_of_books=0
    @decorator
    def addbooks(self):
        bname=input("Enter the name of the book: ")
        self.books.append(bname)
        self.no_of_books=len(self.books)
    def show(self):
        print(f"The no of  books in the library are: {self.no_of_books}")
        print(f"The books in the library are:{self.books} ")
    
lib=library()
i=int(input("Press 1 to add books in the library"))
if i==1:
    lib.addbooks()
    lib.show()
else:
    lib.show()