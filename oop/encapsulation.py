class Car:
    def __init__(self, make, model, year):
        # Constructor method to initialize the attributes of the Car class
        # private attributes are defined with double underscores (__) to indicate that they should not be accessed directly from outside the class. This is a way to implement encapsulation in Python.
        self.__make = make
        self.__model = model
        self.__year = year

    # Method to display the information of the car
    # getters and setters are methods that allow controlled access to private attributes. They provide a way to retrieve (get) and modify (set) the values of private attributes while maintaining encapsulation.
    def display_info(self):
        return f"{self.__year} {self.__make} {self.__model}"

my_car = Car("Toyota", "Camry", 2020)
# Accessing the private attributes directly will raise an AttributeError
#print(my_car.__make)  # This will raise an AttributeError
print("My car is a " + my_car.display_info())

# a example of setting and getting private attributes using getters and setters
class CarWithGettersSetters:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    # Getter method for the make attribute
    def get_make(self):
        return self.__make

    # Setter method for the make attribute
    def set_make(self, make):
        self.__make = make

    # Getter method for the model attribute
    def get_model(self):
        return self.__model

    # Setter method for the model attribute
    def set_model(self, model):
        self.__model = model

    # Getter method for the year attribute
    def get_year(self):
        return self.__year

    # Setter method for the year attribute
    def set_year(self, year):
        self.__year = year

my_car_with_getters_setters = CarWithGettersSetters("Honda", "Civic", 2019)
# Accessing the private attributes using getters and setters
print("My car is a " + str(my_car_with_getters_setters.get_year()) + " " + my_car_with_getters_setters.get_make() + " " + my_car_with_getters_setters.get_model())

# difference between getters and setters and direct access to attributes is that getters and setters provide a controlled way to access and modify private attributes, while direct access allows unrestricted access to public attributes. Getters and setters can include validation logic, while direct access does not.
# in the example above, the Car class uses private attributes and provides a display_info method to access the information of the car. The CarWithGettersSetters class uses getters and setters to provide controlled access to the private attributes.
# setters can be used to validate the input before setting the value of an attribute, while getters can be used to format or process the value before returning it. This allows for better encapsulation and data integrity in object-oriented programming.