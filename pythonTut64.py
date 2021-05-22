class Employee :
    no_of_leaves : 8
    var=20
    _protec=11
    __private=13

    def __init__(self,name,salary,role):
        self.name = name
        self.salary= salary
        self.role=role

    def printDetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and the role is {self.role}"

    @classmethod
    def changes_leaves(cls,newLeaves):
        cls.no_of_leaves=newLeaves

    # @classmethod
    # def from_dasah(cls,string):
    #     return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good "+string)

harry=Employee("Harry",455,"Instructor")
print(harry.name)
print(Employee._protec)
print(harry._protec)
# print(harry.__private)
print(harry._Employee__private)