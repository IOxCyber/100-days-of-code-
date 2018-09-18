try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
    print("Error")
    print("Finished")
finally:  #this'll run after the try n except statement
    print("The output has com no matter what happened")
     
