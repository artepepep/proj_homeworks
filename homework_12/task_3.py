def check_types(func):
    def wrapper(*args, **kwargs):
        if (isinstance(func(*args, **kwargs), str)):
            raise TypeError("Argument a must be int, not str")
    return wrapper
@check_types
def add(a: int, b: int) -> int:
    return a + b
add(1, 2)
add("1", "2")