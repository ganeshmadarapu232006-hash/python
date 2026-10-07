def outer_function():
    def inner_function():
        return "Hello from inner function"

    return inner_function


result = outer_function()
print(result())