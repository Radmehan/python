# def print2(str1) :
#     return "this is "+ str1
# v= print2("Harry")
# print(v)

# def print2(str1) :
#     print("this is ", str1)
# print2("harry")

# def print2(str1) :
#     print2(str1)
#     print("this is ", str1)
# print2("harry")


# n! = n* n-1 * n-2 * n-3 ..........1
# n! = n* (n-1)!


def factorial_Iterative(n) :
     """
     :param n: Integer
     :return: n* n-1 * n-2 * n-3 * ....1
     """

     fac=1
     for i in range(n) :
         fac = fac*(i+1)
     return fac

def factorial_Recursive(n) :

     if n==0 :
          return 1
     else:
          return n * factorial_Recursive(n-1)



#quiz create a fibonacci =0,1,1,2,3,5,8

def fibonacci(n) :
     if n==1:
          return 0
     elif n==2:
          return 1
     else:
          return fibonacci(n-1)+fibonacci(n-2)

number=int(input("Enter the number"))
print("Factorial using iterative method", factorial_Iterative( number))
print("Factorial using recursive method", factorial_Recursive( number))
print("Factorial using fibonacci method", fibonacci(number))