#Error handling i.e Try and Except
try:
    num1 = 8
    num2 =6 
    print (num1 / num2)
    print(num1//num2)
    print(num1 % num2 )
    print("Done calculation\n\n")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")
    
    
    
try:
   variable = 10
   print (10 / 0) 
except ZeroDivisionError:
    print("Error")
    print("Finished")
    
    """
    Output 
    
1.3333333333333333
1
2
Done calculation


Error
Finished
    
    """
