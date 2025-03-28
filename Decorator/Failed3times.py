import time
import functools

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)  # Try executing the function
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts}: {e}")  # Print error message
                    time.sleep(delay)  # Wait before retrying
            raise Exception(f"Function {func.__name__} failed after {max_attempts} attempts")
        return wrapper
    return decorator

# Example usage
@retry(max_attempts=3, delay=2)
def login(username, password):
    """Simulated login function that fails"""
    if username != "admin" or password != "1234":
        raise ValueError("Invalid credentials")
    return "Login Successful"

# Testing the function
try:
    print(login("user", "wrongpass"))  # Will fail 3 times and then raise exception
except Exception as e:
    print("Final Exception:", e)