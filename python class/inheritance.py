class A:
    def m1(self):
        print("A ia class m1 method")
class B(A):
    def m2(self):
        print("child B is derived from A class : m2 method")
obj=B()
obj.m1()
obj.m2()
#======================================================
class A:
    a=0
    b=0
    
    def add(self,a,b):
        self.a=a
        self.b=b
        print("addition is:",self.a+self.b)
class B(A):
    def m1(self):
        self.m=a*b
        print("multiplication is:",self.m)
obj=B()
obj.add()
obj.m1()
        
