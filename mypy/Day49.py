"""
Dictionaries are data structures used to map arbitrary keys to values. 
Lists can be thought of as dictionaries with integer keys within a certain range.
Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
Only immutable objects can be used as keys to dictionaries. Immutable objects are those that can't be changed.
means you can't use the digit eg. ages = {"64":Dave, "42":John}.
Trying to use a mutable object as a dictionary key causes a TypeError.
"""
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
print(ages["John"])

"""
Output
24
42
58
"""
