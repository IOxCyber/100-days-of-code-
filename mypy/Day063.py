#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(4))

#lambda
print((lambda x: x**2 + 5*x + 4) (5))



"""
Lambda functions aren't as powerful as named functions. 
They can only do things that require a single expression - usually equivalent to a single
line of code.

"""

#you can assign lambda into a variale too
double = lambda x: x * 2
print(double(7))

