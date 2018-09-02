#FUNCTIONS
#1
nums = [1, 2, 3]
nums.append(4)
print(nums)    #add an item @ the end
                   

#2
nums = [1, 3, 5, 2, 4]
print(len(nums)) #to cal the length of the array

#3
words = ["Python", "fun"]
#index = 1
words.insert(1, "is") #it takes 2 arg. & u can insert any item @ any index
print(words)

#4
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))   #index used to find the item in the list & return the index value
print(letters.index('p'))   #if there's no item found shows error.
print(letters.index('z'))   #as here show a error.



# output
# [1, 2, 3, 4]
# 5
# ['Python', 'is', 'fun']
# 2
# 0

Traceback (most recent call last):
  File "..\Playground\", line 22, in <module>
    print(letters.index('z'))   #as here show a error.
ValueError: 'z' is not in list
