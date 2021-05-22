class Employee :
    no_of_leaves : 8
    var=9

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

class Player :
    no_of_games=4
    var=10
    def __init__(self,name,games):
        self.name=name
        self.games=games

    def printDetails(self):
        return f"The name is {self.name}. Game is {self.games}"

class coolProgrammer(Employee,Player) :
# class coolProgrammer( Player,Employee):
    var=11
    language="C++"
    # def printLanguage(self):
    #     print(self.language)
    def printLanguage(self,languages):
        self.language=languages



shuvam=Player("Shuvam",["Cricket"])
karan=coolProgrammer("Karan",999,"Coolprogrammer")
details=karan.printDetails()

print(details)
print(karan.language)
print(karan.var)
