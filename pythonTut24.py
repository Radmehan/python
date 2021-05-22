"""a=9
b=7
# c=sum(a,b)

c=sum((a,b))
print(c)"""

"""def func1():
    print("hello you are in func1")

# print(func1())
func1()"""

"""
def func2(a,b):
    print("hello you are in func1 \n", a+b)

func2(5,7)"""

"""
def func3(a,b):
    average=(a+b)/2
    print(average)
func3(9,7)
#v=func3(9,7)
#print(v)
"""

def func4(a,b):
    """This function which will calculate average of two number.
    this function doesn't work for three number"""
    average=(a+b)/2
    return average

result=func4(6,6)
print(result)
print(func4.__doc__)