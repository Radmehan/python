# files1 = open("harry.txt")
# content= files1.read()
# files1 = open("harry.txt", "rb")
files1 = open("harry.txt", "rt")
# content = files1.read()

# content = files1.read(3)
# print(content)

# content = files1.read(3)
# print(content)

# content = files1.read(3334)
# print("1", content)
# content = files1.read( 3334)
# print("2",content)

#content = files1.read()
# for line in content:
#     print(line)
# files1.close()

# for line in files1:
#     print(line, end=" ")

# content= files1.readline()
# print(content, end="")
# content= files1.readline()
# print(content, end="")
# content= files1.readline()
# print(content, end="")
content= files1.readlines()
print(content, end="")

files1.close()