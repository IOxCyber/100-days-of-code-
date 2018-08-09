#if statement

if 10 > 5:
print("10 greater than 5")


#here no need to add curly braces it uses white space( ) and Colon (:) at the end.
#output 
#10 greater than 5


#nested of if 

num = 15
if num > 9:
    print("Bigger than nine")
    if num <=50:
        print("and num is between nine and fifty ")
#output 
#Bigger than nine and num is between nine and fifty



#if else statement

num = 7
if num == 5:
    print("Number is 5")
else: 
    if num == 11:
        print("Number is 11")
    else:
        if num == 7:
            print("Number is 7")
        else: 
            print("Number isn't 5, 11 or 7")

#output 
#Number is 7
