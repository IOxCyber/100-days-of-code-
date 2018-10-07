def apply_twice(func, arg):
    return func(func(arg))

"""
    Think As:
    return add_five(add_five(10))
    return add_five(16)
    return 22 //so answer is 22.
    
    
    In functional programming we can pass the function as arguments.
"""
    
def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))
