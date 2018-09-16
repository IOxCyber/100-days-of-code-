# Returning from Function
#Here we have defined the function called as "max"
#and Called the function 2 times i.e in print() and to the Variable Z too. 

def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))
z = max(8, 5)
print(z)
#output
#7
#8
