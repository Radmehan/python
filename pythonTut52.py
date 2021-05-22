# def function1():
#     print("Subscribe now")
#
# func2=function1
# del function1
# func2()

# def funret(num):
#     if num == 0 :
#         return print
#     if num == 1 :
#         # return int
#         return sum
# a=funret(0)
# a=funret(1)
# print(a)

# def executor(func) :
#     func("This")
# executor(print)

def dec1(func1) :
    def nowexec() :
        print("Excuting now")
        func1()
        print("Excuted")
    return nowexec
@dec1
def who_is_harry() :
    print("Harry is good boy")

# who_is_harry()
# who_is_harry = dec1(who_is_harry)

who_is_harry()

