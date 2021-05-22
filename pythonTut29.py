# files=open("harry.txt")
# content=files.read()
# print(content)

# files=open("harry2.txt","w")
# files=open("harry2.txt", "a" )
# a=files.write("Hello Harry\n")
# print(a)
# files.close()

# files=open("harry2.txt","w")
# a=files.write("Harry is one of the best guy")
# print(a)

# open file read and write
files=open("harry2.txt", "r+")
print(files.read())
files.write("Thank you\n")
