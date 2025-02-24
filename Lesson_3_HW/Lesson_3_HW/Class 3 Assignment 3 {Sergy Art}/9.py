def flexible_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

user_name = input("What is your name?")

@flexible_decorator
def greet(name):
    print(f"Hello, {name}!")

greet(user_name)