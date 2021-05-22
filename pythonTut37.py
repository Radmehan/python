"""
Anonymous or lambda function

"""

def add(a,b) :
    return a+b
print(add(9,5))

def minus(a,b) :
    return a-b
print(minus(9,5))

minus = lambda x,y: x-y
print(11-5)

plus =lambda x,y : x+y
print(11+6)

def a_first(a):
    return a[1]

# a = [[1, 4], [5, 6], [8,23]]
# a.sort(key=a_first)
a = [[1, 14], [5, 6], [8,23]]
a.sort(key=lambda x:x[1])
print(a)