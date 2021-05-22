class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@codewithharry.com"
    def explain(self):
        return f"The employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set please set your email.........."
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self,string):
        print("Setting now")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


harry=Employee("Harry", "Coder")
rohan=Employee("Rohan", "Chy")
print(harry.explain())
print(harry.email)
harry.fname="US"
# print(harry.email())
print(harry.email)

harry.email="This.that@codewithharry.com"
print(harry.fname)
print(harry.email)

del harry.email
print(harry.email)



