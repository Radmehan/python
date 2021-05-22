# f = open("does.txt")
# print(f)
""""
try :
    f=open("does.txt")
except Exception as e:
    print(e)
print("Important stuff")
"""

"""
f1=open("harry.txt")
try :
    f=open("does.txt")
except Exception as e:
    print(e)
else:
    print("This will run only if except is not working")
finally:
    print("Run this anyway")
print("Important stuff")
"""

f1=open("harry.txt")
try :
    f=open("does2.txt")
# except Exception as e:
#     print(e)
except EOFError as e:
    print("EOFerror comes",e)
except IOError as e:
    print("IOerror comes", e)
else:
    print("This will run only if except is not working")
finally:
    print("Run this anyway")
print("Important stuff")