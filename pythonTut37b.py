"""
Anonymous or lambda function practice

"""
def add(a,b):
     return a+b
print(add(5,10))

add=lambda x,y : x+y

print(add(5,10))

def minus(c,d):
    return c-d
print(minus(20,10))

minus = lambda m,n : m-n
print(minus(20,10))

def first_a(a):
    # return a[0]
    return a[1]

a=[[1,14],[5,6],[8,23]]
a.sort(key=first_a)
print(a)

x=[[1,14],[5,6],[8,23]]
x.sort(key=lambda b:b[1])
print(x)

