myList=["harpic", "Vim", "deodrant", "vindi", "lollypop", 56]
print(myList)
#print(myList[2])
"""
print(myList.sort())
print(myList)"""
#myList.reverse()
#print(myList)

#slice
# positive index
"""print(myList[:])
print(myList[0:])
print(myList[:4])
print(myList[1:4])

#Extended slice
print(myList[::1])
print(myList[::2])
print(myList[::3])
print(myList[::-3])
print(myList[::-2])
print(myList[1:5:-3])
print(myList[1:5:-1])"""

#negetive index
"""print(myList[-3:])
print(myList[:-3])
print(myList[-5:-1])"""

# Added index
"""myList.append(67)
print(myList)
myList.insert(4,"ai")
print(myList)
myList.remove("deodrant")
print(myList)"""
#myList.pop()
#print(myList)
"""myList.pop(2)
print(myList)
del myList[2]
print(myList)"""

print(len(myList))
myList2=[2,3,4,5,6]
myList.append(myList2)
print(myList)
for x in myList:
    print(x)