class Employee :
    no_of_leaves : 8

    def __init__(self,name,salary,role):
        self.name = name
        self.salary= salary
        self.role=role

    def printDetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and the role is {self.role}"

    @classmethod
    def changes_leaves(cls,newLeaves):
        cls.no_of_leaves=newLeaves

    @classmethod
    def from_dasah(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good "+string)

harry=Employee.from_dasah("Harry-455-Instructor")
rohan=Employee.from_dasah("Rohan-480-student")
karan=Employee.from_dasah("Karan-460-student")
Employee.no_of_leaves=34

harry.printGood("Harry")
# print(Employee.__dict__)
print(harry.__dict__)
print(karan.__dict__)
print(karan.printDetails())
print(harry.no_of_leaves)