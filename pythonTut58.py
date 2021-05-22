class Employee :
    no_of_leaves=8

    def __init__(self,givenName,givenSalary,givenRole):
        self.name=givenName
        self.salary=givenSalary
        self.role=givenRole

    def printDetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newLeaves):
        cls.no_of_leaves =newLeaves

    @classmethod
    # def from_dash(cls,string):
    #     params=string.split("-")
    #     print(params)
    #     return cls(params[0], params[1], params[2])
    def from_dash(cls,string):
        return cls(*string.split("-"))




harry=Employee("Harry",455,"Instructor")
rohan=Employee("Rohan",345,"Student")
karan=Employee.from_dash("Karan-480-student")
print(karan.printDetails())


