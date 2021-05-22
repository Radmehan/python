"""
print("Enter number a")
a=int(input())
print("Enter number b")
b=int(input())
print("The sum of these two number is ",a+b)
"""

print("Enter number a")
a=input()
print("Enter number b")
b=input()
try:
    print("The sum of these two number is ",
          int(a)+int(b))
except Exception as e:
    print(e)

print("this line is very important")