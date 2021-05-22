"""
a=input("What's your name? : ")
if a.isnumeric():
    raise Exception("Numbers is not allow")

#1000 lines taking 1 hour
print(f"hello {a}")"""

"""
a=input("What's your name? : ")
b=int(input("How much do you earn : "))
if b==0:
    raise ZeroDivisionError("b is zero so stopping the program")
if a.isnumeric():
    raise Exception("Numbers is not allow")

#1000 lines taking 1 hour
print(f"hello {a}")"""

c=input("Enter your name : ")
try:
    print(a)

except Exception as e:
    if c=="harry":
        raise ValueError("Harry is blocked. He is not allowed")
    print("Exception handled")
