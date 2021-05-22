# def function_name_print(a,b,c,d) :
#     print(a,b,c,d)
#
# function_name_print("Harry","Rohan", "Shuvam", "Hammad")

# def function_name_print(a,b,c,d) :
#     print(a,b,c,d)
#
# function_name_print("Harry","Rohan", "Shuvam", "Hammad","Skillf")

# def function_name_print(a,b,c,d,e) :
#     print(a,b,c,d,e)
#
# function_name_print("Harry","Rohan", "Shuvam", "Hammad","Skillf")

# def funcArgs(*args):
#     # print(args[0])
#     for item in args:
#         print(item)
#
# har=["Harry","Rohan", "Shuvam", "Hammad","Skillf","The programmer"]
# funcArgs(*har)

# def funcArgs(normal,*args):
#     # print(args[0])
#     print(normal)
#     for item in args:
#         print(item)
# normal="I am a normal argument and these students are"
# har=["Harry","Rohan", "Shuvam", "Hammad","Skillf","The programmer"]
# funcArgs(normal,*har)

def funcArgs( normal,*argsRohan,**kwargs):
    # print(args[0])
    print(normal)
    for item in argsRohan:
        print(item)
    print("\nNow I would like to meet our heroes : ")
    for key,value in kw.items():
        print(f"{key} is {value}")
kw={
    "Harry" : "Monitor",
    "Rohan" : "fitness",
    "The programmer" : "Co-ordinate"
}
normal="I am a normal argument and these students are"
har=["Harry","Rohan", "Shuvam", "Hammad","Skillf","The programmer"]
funcArgs(normal,*har,kw)