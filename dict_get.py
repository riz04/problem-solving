# a program to understand use of keyword arguments
# use of dict.get() 
# dict.get('first') will return the value of 'first' if it exists, otherwise it returns None
# However, we can specify a second argument which will replace None as the default value.

def calculate(**kwargs):
    print(kwargs)

    operation_lookup = {
            'add': kwargs.get('first', 0) + kwargs.get('second', 0),
            'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
            'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
            'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
                       }
    operation_value = operation_lookup[kwargs.get('operation')]
    

    is_float = kwargs.get('is_float', False)
    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message','The result is')} {int(operation_value)}"
    return final


print(calculate(first = 4 , operation = "subtract", second = 7))