class Car:
    # Constructor method to initialize the attributes of the Car class
    # __init__ is a special method in Python classes that is called when an object is created. It allows you to set the initial state of the object by assigning values to its attributes.
    # self is a reference to the current instance of the class. It allows you to access the attributes and methods of the class within its own methods.
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Bugatti", "Chiron", 2021)
print("My car is a " + str(my_car.year) + " " + my_car.full_name())