import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record end time
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result  # Return the original function's result
    return wrapper

# Example usage
@execution_time_decorator
def example_function(n):
    total = sum(range(n))  # Sample computation
    return total

# Calling the function
print("Result:", example_function(1000000))