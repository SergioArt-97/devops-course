import time


def function_time(message = "Execution time:"):
    def decorator(function):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time()
            total_time = end_time - start_time
            print(f"{message} {total_time:.6f} seconds")
            return result
        return wrapper
    return decorator

@function_time()
def sum_numbers():
    return sum(range(1,1000000))

@function_time(message="Custom message - Time taken to execute")
def sum_numbers_custom_message():
    return sum(range(1,1000000))


sum_numbers()
sum_numbers_custom_message()