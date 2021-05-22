s=set()
#print(type(s))
#s_from_list = set([1,2,3,4])
l=[1,2,3,4,5,6]
s_from_list=set(l)
print(s_from_list)
#for x in s_from_list:
    #print(x)
s.add(1)
s.add(2)
print(s)
#s1=s.union({1,2,3})
#s1=s.union(s_from_list)
s1=s.intersection(s_from_list)

print(s,s1)
print(len(s1))
s_from_list.remove(5)
print(s_from_list)