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

class ElectricCar(Car):
    # Constructor method to initialize the attributes of the ElectricCar class
    # The super() function is used to call the constructor of the parent class (Car) and initialize its attributes.
    def __init__(self,brand,model,year,battery_size):
        super().__init__(brand,model,year)
        self.battery_size = battery_size

    # def full_name(self):
    #     return f"{self.brand} {self.model} with a {self.battery_size}-kWh battery"


electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
print("My electric car is a " + str(electric_car.year) + " " + electric_car.full_name())