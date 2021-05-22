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


harry=Employee("Harry",455,"Instructor")
rohan=Employee("Rohan",345,"Student")

print(harry.printDetails())
print(rohan.printDetails())
print(harry.no_of_leaves)

# Employee.no_of_leaves=89
# print(harry.no_of_leaves) #after change value

harry.change_leaves(34)
print(harry.no_of_leaves)
print(Employee.no_of_leaves)

