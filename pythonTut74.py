ls=[]
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)

ls2=[i for i in range(100) if i%3==1 ]
print(ls2)

dict={
i: f"item {i}"
    for i in range(100) if i%5==0
}
print(dict)

dict2={
    i : f"item{i}"
    for i in range(1,5)
}
print(dict2)

dict3={
    value:key for key,value in dict2.items()
}
print(dict3)

dresses={
    dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]
}
print(dresses)
print(type(dresses))

evaens=(i for i in range(1,1000) if i%2==0 )
print(evaens)
print(type(evaens))
print(evaens.__next__())
print(evaens.__next__())
print(evaens.__next__())
print(evaens.__next__())
print(evaens.__next__())
print(evaens.__next__())

# for item in evaens:
#     print(item)
