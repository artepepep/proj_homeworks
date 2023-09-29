from inspect import signature
def check_types(func):
    def wrapper(a, b):
        pass
    sig = signature(wrapper)
    str(sig)
    str(sig.parameters['a'])
    if sig.parameters['a'].annotation != 'int' and sig.parameters['b'].annotation != 'int':
        raise TypeError("Argument a must be int, not str")
    elif sig.parameters['a'].annotation == 'int' or sig.parameters['b'].annotation != 'int':
        raise TypeError("Argument a must be int, not str")
@check_types
def add(a: int, b: int) -> int:
    return a + b
add(3, 4)
add("1", "2")