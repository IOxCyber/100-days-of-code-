# Contents of a file that has been opened in text mode can be read using the read method.
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close() 
#This will print all of the contents of the file "filename.txt".

"""
To read a certain part of a file,U can provide a num as an argument to the read function
This determines the number of bytes that should be read. 
If there is no argument, read returns the rest of the file.
(-ve) values'll return entire contents.
A file have been read, any attempts to read further from that file will return an empty
string
"""
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()


"""
To retrieve each line in a file, you can use the readlines method to return a list
in which each element is a line in the file.
"""
file = open("filename.txt", "r")
print(file.readlines())
file.close()
