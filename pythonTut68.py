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

    # @classmethod
    # def from_dasah(cls,string):
    #     return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good "+string)

    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary / other.salary
        # return other.salary / self.salary

    def __str__(self):
        return self.printDetails()

    def __repr__(self):
        return f"Employee('{self.name}','{self.salary}','{self.role}')"




emp1=Employee("Harry",455,"programmer")
emp2=Employee("Rohan",434,"Student")

# print(emp1+emp2)
print(emp1+emp2)
print(emp1/emp2)
print(emp1)
print(emp2)
print(str(emp1))
print(repr(emp1))
# print(str(emp1))  #after commenting Str