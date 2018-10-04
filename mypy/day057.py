#string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

#You can do formatting with the "Named Argument".
a = "{x}, {y}".format(x=5, y=12)
print(a)

"""
1.Define a list.
2.Take a variable & assign the string and the value in ordered manner.
3.Concatinate with the "FORMAT" keyword & pass the list index wise.

4.If you omit the value in curley braces then it'll show error.


OUTPUT
Numbers: 4 5 6
5, 12
"""
