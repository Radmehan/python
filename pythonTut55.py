class Employee :
    no_of_leaves=8
    pass
harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=455
harry.role="Instructor"

rohan.name="Rohan"
rohan.salary=345
rohan.role="Student"

print(rohan.name, harry.salary)
print(harry.no_of_leaves, rohan.no_of_leaves)
print(Employee.no_of_leaves)

# rohan.no_of_leaves=8
print(Employee.no_of_leaves)

print(rohan.__dict__)
rohan.no_of_leaves=9
print(rohan.__dict__)

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves=9
print(Employee.__dict__)
print(Employee.no_of_leaves)
