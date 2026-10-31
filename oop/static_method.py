# static method is a method that belongs to a class rather than an instance of the class. It does not require access to the instance (self) or class (cls) variables. Static methods are defined using the @staticmethod decorator and can be called on the class itself without creating an instance.
# self is not passed as the first argument to static methods, and they cannot access or modify instance or class-level data. Static methods are often used for utility functions that perform a task in isolation.
# we can protect any method using decorators. Decorators are a way to modify or enhance the behavior of functions or methods. In Python, decorators are defined using the @ symbol followed by the decorator function name. They can be used to add functionality, enforce access control, or perform other tasks before or after the execution of the decorated method.

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    # @staticmethod decorator is used to define a static method that performs division. It takes two parameters, a and b, and checks if b is zero to avoid division by zero errors. If b is zero, it raises a ValueError; otherwise, it returns the result of dividing a by b.
    # decorator is used to define a static method that performs division. It takes two parameters, a and b, and checks if b is zero to avoid division by zero errors. If b is zero, it raises a ValueError; otherwise, it returns the result of dividing a by b.
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    # @property decorator is used to define a property method that allows access to the result of a static method as if it were an attribute. It calls the divide static method with predefined values (10 and 2) and returns the result. This allows users to access the division result without explicitly calling the divide method.
    # read-only property that allows access to the result of the divide static method without explicitly calling it. It calls the divide method with predefined values (10 and 2) and returns the result.
    @property
    def division_result(self):
        return self.divide(10, 2)
    
# Example usage:
result_add = MathOperations.add(5, 3)
result_subtract = MathOperations.subtract(10, 4)
result_multiply = MathOperations.multiply(6, 7)
try:
    result_divide = MathOperations.divide(8, 0)
except ValueError as e:
    result_divide = str(e)  


print("Addition Result:", result_add)
print("Subtraction Result:", result_subtract)
print("Multiplication Result:", result_multiply)
print("Division Result:", result_divide)

print("Division Result (Property):", MathOperations().division_result)