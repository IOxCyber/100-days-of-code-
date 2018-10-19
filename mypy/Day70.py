
#Example of Recursion


#Infinite
def factorial(x):
    return x * factorial(x-1)

print(factorial(5))
r
#Non infinite
def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)
    
print(factorial(5))
