def sum_two_numbers(a, b):
    return a + b    

def subtract_two_numbers(a, b):
    return a - b    

def multiply_two_numbers(a, b):
    return a * b

def divide_two_numbers(a, b):
    if b == 0:
        raise ValueError("Division par zero n'est pas autorisee.")
    return a / b    


