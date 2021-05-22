# def func1(n) :
#     return n+" "+ "I have printed"
#
# print(func1("This is me"))

 # l=10       #global veriable

# def func1(n) :
#     l=5   #local veriable
#     m=8     #local veriable
#     print(l)
#     print(n, "this is me")
#
# func1("This is me")
# print(l)


# l=10
#
# def func1(n) :
#     # l=5
#     m=8
#     print(l)
#     print("I have printed")
# func1("This is me")
# print(l)



# l=10
#
# def func1(n) :
#     # l=5
#     m=8
#     l=l+45
#     print(l)
#     print("I have printed")
# func1("This is me")
# print(l)





l=10

def func1(n) :
    # l=5
    m=8
    global l
    l=l+45
    print(l,m)
    print("I have printed")
func1("This is me")
print(l)