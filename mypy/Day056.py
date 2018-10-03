"""
List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
List comprehensions are inspired by set-builder notation in mathematics.
"""
varcube = [i**3 for i in range(5)]
print(varcube) #print cubes b/w 0 to 5

#you can use if in list comprehensions.
varmul=[i*2 for i in range(10) if i*2 % 2 == 0]
print(varmul) #print even no. b/w 0 to 18


#Trying to create a list in a very extensive range will result in a MemoryError.
var = [2*i for i in range(10**100)] #gives memory exceed error.
