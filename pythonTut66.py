class A :
    classVar1="I'm class variable in class A"
    def __init__(self):
        self.var1="I'm inside class A's constructor"
        self.classVar1="Instance var in class A"
        self.special="Special"

class B(A):
    classVar2="I'm in class B"

    def __init__(self):
        super().__init__()
        self.var1="I'm inside class B's constructor"
        self.classVar1="Instance var in class B"
        # print(super().classVar1)
        # super().__init__()

a=A()
b=B()

print(b.classVar1)
print(b.special,b.var1,b.classVar1)