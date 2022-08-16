def multiply(n):
    def inner(func):
        def decorator(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * n
        return decorator
    return inner


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))



