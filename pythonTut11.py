# myDic = {}
myDic={
    'name':'Harry',
    'age':32,
    'Rohabn':'fish',
    'skilf':'ruti'
}
print(myDic)
print(myDic['name'])
print(myDic['age'])

myDic2 = {
    "Harry": 'Burgrer',
    "Rohan": "fish",
    'Rohabn':'fish',
    'skilf':'ruti',
    "Shuvom":{
        "b":"maggie", "l":"ruti", "d" :"chiken"
    }
}
print(myDic2)
"""
print(myDic2["Shuvom"])
print(myDic2["Shuvom"]["b"])
myDic2["Ankit"]="junkfood"
print(myDic2)
myDic2["Auron"]="kabab"
print(myDic2)
myDic2[430]="Singara"
print(myDic2)

del myDic2[430]
print(myDic2)"""

#myDic3 = myDic2
#del myDic3['Harry']
#print(myDic3)
"""
myDic3=myDic2.copy()
myDic3=myDic2
del myDic3['Harry']
print(myDic3)

print(myDic2.get("Harry"))
#print(myDic2.update({"Linax": "software"}))

myDic2.update({"Linax": "software"})
print(myDic2)
print(myDic2.items())
print(myDic2.keys())"""
#for item in myDic2:
   # print(item)
for item,value in myDic2.items():
    print(item,":",value)