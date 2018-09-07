#1
def hello():  # def is used to define a user define function
    print("Hello world!") #write in the same way like just below the hello name
    
    hello()
#output
#Hello world!
#2
def print_this(word):
  print("This is " + word+".")
print_this("spam")
print_this("eggs")
print_this("python")

#3 
def print_calc(x, y):    
  print(x - y)
  print(x * y)   
  print(x + y)
  
print_calc(8, 3)  

#here we have taken two arg with that we're calculating sum,sub,multiply operation.  
#output
#This is spam.
#This is eggs.
#This is python.
#5
#24
#11
