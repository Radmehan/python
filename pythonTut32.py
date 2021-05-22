# files = open("harry.txt")
# con=files.read()
# print(con)
# files.close()

# with open("harry.txt") as files :
#     con=files.read()
#
# print(con)
# files.close()

with open("harry.txt","r") as files1 :
    con= files1.readlines()
    print(con)
files1.close()