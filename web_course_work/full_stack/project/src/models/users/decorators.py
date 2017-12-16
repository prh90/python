from functools import wraps


def requires_login(func):
    @wraps(func)
    def decorated_function():
        pass

@requires_login
def my_function():
    print("Hello World!")
    return "Hi"