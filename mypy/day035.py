def add(x, y):
    return x + y

def do_twice(arg, x, y): #we have added the func here as args
    return arg(arg(x, y), arg(x, y))

a = 5
b = 10

print(add(a, b))
print(do_twice(add, a, b))
# here in the print fun the actual args replace the formal args. 
