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


class Programmer(Employee) :

    def __init__(self,name,salary,role,languages):
        super().__init__(name,salary,role)
        self.languages=languages



    def printProg(self):
        return f"The programmer's name is {self.name}. Salary is {self.salary} and the role is {self.role}. The languages are {self.languages}"


# harry=Employee.from_dasah("Harry-455-Instructor")
# rohan=Employee.from_dasah("Rohan-480-student")
# karan=Programmer.from_dasah("Karan-460-student-['Python']")

harry=Employee("Harry",455,"Instructor")
rohan=Employee("Rohan",480,"student")
# karan=Programmer("Karan",460,"student","['Python']")
# shuvam=Programmer("Shuvam",4555,"Programmer",["Python","C++"])
shuvam=Programmer("Shuvam",4555,"Programmer",["Python","C++"])

print(shuvam.printProg())
print(shuvam.name)
shuvam.printGood("Shuvam")