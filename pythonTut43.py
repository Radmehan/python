import time

# initial=time.time()
# print(initial)
#
# i=1
# while i<=45 :
#     print(i,"This is Harry vai")
#     i+=1
# print("Now printing while loop",time.time()-initial)
#
# initial2=time.time()
# for i in range(45+1) :
#     print(i, "This is Harry vai")
# print("\nNow printing for loop",time.time()-initial2)

loc=time.asctime(time.localtime(time.time()))
print(loc)
