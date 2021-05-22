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

skill=Employee("skill","F")
print(skill.email)
print(type(skill))
print(id(skill))
print(id("this is string"))
print(id("this that"))
print(id("this that"))
print(id("This that"))

o="this is string"
print(dir(o))
print(dir(skill))

import inspect
print(inspect.getmembers(skill))