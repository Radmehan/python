"""
i=0
while(True):
    if i+1<5:
        i+=1
        continue
    print(i+1, end=" ")
    if(i+1==44):
        break #stop the loop
    i+=1
    """

#quiz


while(True):
    inp=int(input("enter a number\n"))
    if(inp>100):
        print("congrats you have entered a number greater than 100\n")
        break
    else:
        print("try again!\n ")
        continue