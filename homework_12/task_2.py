def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print ("no such key")
    return wrapper
@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])
some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})