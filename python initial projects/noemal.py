# Create a class
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"hello my name is {self.name}")
# Create an object
p1=person("akshat",18)
# Call the greet method
p1.greet()
