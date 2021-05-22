# class Employee :
#     no_of_leaves=8
#
#     def printDetails(self):
#         return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     # def printDetails():
#     #     return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#
# harry=Employee()
# rohan=Employee()
#
# harry.name="Harry"
# harry.salary=455
# harry.role="Instructor"
#
# rohan.name="Rohan"
# rohan.salary=345
# rohan.role="Student"
#
# print(rohan.printDetails())
# print(harry.printDetails())

# =============CONSTRUCTOR=============

class Employee :
    no_of_leaves=8

    def __init__(self,givenName,givenSalary,givenRole):
        self.name=givenName
        self.salary=givenSalary
        self.role=givenRole


    def printDetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry=Employee("Harry",455,"Instructor")
rohan=Employee("Rohan",345,"Student")

# harry.name="Harry"
# harry.salary=455
# harry.role="Instructor"
#
# rohan.name="Rohan"
# rohan.salary=345
# rohan.role="Student"

print(harry.printDetails())
print(rohan.printDetails())
