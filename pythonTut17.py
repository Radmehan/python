list=["harry","larry","marie","carry"]
#print(list[0])
for item in list:
    print(item)

list2=[["harry",2],["larry",6],["marie",10],["carry",250]]
#for items,lollypop in list2:
   # print(items,"and lolly is",lollypop)

myDic= dict(list2)
print(myDic)
#for item,lollypop in myDic.items():
     #print(item, "and lolly is", lollypop)

for item in myDic:
    print(item)

#quiz
list3=["harry","larry","marie","carry",2,3,4,5,6,7,8,98]
for items in list3:
    if str(items).isnumeric() and items>=6:
        print(items)