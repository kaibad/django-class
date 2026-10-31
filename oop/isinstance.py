# problem: Demonstrate the use of instance() to check if my_tesla is and instance of a Car and Electric Car.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model 

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size 


my_tesla = ElectricCar("Tesla", "Model S", 100)
print(isinstance(my_tesla, Car))        # True
print(isinstance(my_tesla, ElectricCar)) # True