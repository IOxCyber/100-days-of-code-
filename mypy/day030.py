# WHILE

words = ["hello", "world", "this","is","my", "life"]
counter = 0
maxIndex = len(words) - 1 

while counter <= maxIndex:   
    word = words[counter]   
    print(word + "!") 
    counter = counter + 1
   

# FOR
# 1.

words = ["hello", "world", "spam", "eggs"]
print("\n")

for word in words:     # it's like the foreach in other language.
    print(word + "!")
    
    
# 2.
print("\n")
for i in range(5):  # it isn't being indexed, so a list isn't required.
    print("hello!")


#OUTPUT
hello!
world!
this!
is!
my!
life!


hello!
world!
spam!
eggs!


hello!
hello!
hello!
hello!
hello!
