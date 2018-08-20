#ex. of while loop 

i = 1
while i <=5:
    print(i)
    i = i + 1

print("loop ended\n\n")

#ex. of Break statement

i = 0
while True:
  print(i)
  i = i+1
  if i >= 5:
    print("Breaked")
    break

print("You are out from loop\n\n")

#ex. of continue statement

i = -1
while True:
   i = i +1
   if i == 2:
    print("Skipped")    #the 2nd  skipped
    continue
   if i == 5:            #If statement will only start executing when i's value reached @5.
      print("Breaking")
      break
   print(i)
