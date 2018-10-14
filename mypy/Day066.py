def pows(x):
    return 2**x

nums = [0, 1, 2, 3, 4, 5]
result = list(map(pows, nums)) #map only apply on iterable value here nums.
print(result)


#With Lambda Function
nums = [5, 4, 3, 2, 1,0]
result = list(map(lambda x: 2**x, nums))
print("\n")
print(result)
print("\n")


#Filter
num = [10, 21, 32, 43, 54]
def div(x):
  if(x%2==0):
    return True

result = list(filter(div, num))
print(result)
print("\n")

result = list(filter(lambda x: x%2==0, num))
print(result)
"""a function that returns a Boolean True will return as result.
it'll only print that is divisible by 2 hence it'll return True &print on the screen.""" 
