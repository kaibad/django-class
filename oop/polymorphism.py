# polymorphism is the ability of an object to take on many forms. In Python, polymorphism allows us to define methods in the child class with the same name as defined in their parent class. This allows us to use the same method name for different types of objects, and the appropriate method will be called based on the object that is being used.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def fuel_type(self):
        return "Gasoline"

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"

my_car = Car("Toyota", "Camry", 2020)
my_electric_car = ElectricCar("Tesla", "Model S", 2021, 100)

print("My car is a " + str(my_car.year) + " " + my_car.brand + " " + my_car.model + " and it runs on " + my_car.fuel_type())
print("My electric car is a " + str(my_electric_car.year) + " "+ my_electric_car.brand + " " + my_electric_car.model + " and it runs on " + my_electric_car.fuel_type())