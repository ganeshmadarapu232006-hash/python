def outer_function():
    def inner_function():
        print("Hello from the inner function!")

    return inner_function


result = outer_function()
result()