numbers = ["3", "34", "64"]

# print(int(numbers[2])+1)

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[2]=numbers[2]+1
# print(numbers[2])

numbers=list(map(int, numbers))
numbers[2]=numbers[2]+1
# print(numbers[2])

# ================MAP===============

# def sq(a) :
#     return a*a
# num=[2,3,5,6,76,3,3,2]
# square = list(map(sq,num))
# print(square)

# num=[2,3,5,6,76,3,3,2]
# square = list(map(lambda x: x*x,num))
# print(square)

# def square(a) :
#     return a*a
#
# def cube(a) :
#     return a*a*a
#
# func = [square,cube]
#
# for i in range(5) :
#     print(i, end=" ")
#     val = list(map(lambda x: x(i), func))
#     print(val)

# ================FILTER===============
# list1 = [1,2,3,4,5,6,7,8,9]
# def is_greater_5(num) :
#     return num>5
# gr_than_5 = list(filter(is_greater_5,list1))
# great_than_5 = list(map(is_greater_5,list1))
# print(gr_than_5)
# print(great_than_5)

# ================REDUCE===============
from functools import reduce

list1 =[1,2,3,4]
list2 =[1,2,3,4,7]
list3 =[1,2,3,4,7]
# num=0
# for i in list1 :
#     num = num+i
# print(num)

num=reduce(lambda x,y : x+y, list1)    #1+2+3+4 = 10
num2 = reduce(lambda x,y: x+y, list2)
num3 = reduce(lambda x,y: x*y, list2)  #1*2*3*4*7 = 168

print(num)
print(num2)
print(num3)