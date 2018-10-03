"""
List slices provide a more advanced way of retrieving values from a list.
Eg. [0:9] here the value will show as including Zero to "8th" index  only not "9th" placed
value....U can remember it as include 1st but not last as in real life people used to do.
"""

var = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(var[2:6])
print(var[3:8])
print(var[ :9]) #here I've omitted the 1st value by default it included all till (last-1).
print(var[0:1])
print(var[0: ]) #on omitting last index's value,print entire list elements. 
print(var[0::2]) #List slices can also have a third number, representing the step, to include only alternate values in the slice.
