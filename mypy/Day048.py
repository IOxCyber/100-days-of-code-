# To write in file you use the write method, which writes a string to the file.
# When a file is opened in write mode, the file's existing content is deleted.
file = open("newfile.txt", "w") #open file
file.write("Some new text") #write this string
file.close()                #close this file

file = open("newfile.txt", "r") #read the file
print("Reading new contents") #print this string
print(file.read()) #read this file
print("Finished") #print this
file.close() #close after operations


msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg) #write method return num. of bytes written to a file.
print(amount_written) 
file.close()
