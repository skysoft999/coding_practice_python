
def add(x, y):
    """Add function"""
    return x + y

def substract(x, y):
    """substract Function"""
    return x - y

def multiply(x, y):
    """multiply Function"""
    return x * y 

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x / y