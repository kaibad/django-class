# problem: Create a decorator to print the name of the function and the values of the arguments passed to it every time the function is called.

def log_function_call(func):
    def wrapper(*args,**kwargs):
        #join method gives a list of strings and joins them with a separator, in this case a comma and a space.
        args_values = ", ".join(str(args) for args in args)
        kwargs_values = ", ".join(f"{k}={v}" for k,v in kwargs.items())

        print(f"Function '{func.__name__}' called with arguments: {args_values} and keyword arguments: {kwargs_values}")
 
        return func(*args,**kwargs)

    return wrapper


@log_function_call
def greet(name,greeting="hello"):
    print(f"{greeting}, {name}!")

greet("Kailash",greeting="Hi")  # Output: Hi, Kailash!