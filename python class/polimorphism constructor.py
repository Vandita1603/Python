'''class demo:
    def __init__(self):
        print("no argument constructor ")
    def __init__(self,a):
        print("one argument constructor ")
    def __init__(self,a, b):
        print("two argument constructor ")
#d=demo()
d=demo(10,20)'''
#===============================================================
'''class demo:
    def __init__(self,a=None,b=None,c=None):
        print(a)
        print(b)
        print(c)
d1=demo(10,20)
d2=demo(10,20,30)
d3=demo(10)
'''
#========constructor with variable length object=============================
'''class demo:
    def __init__(self,*a):

        print("constructor with variable number of arguments")
d=demo()
d2=demo(10,20)
d3=demo(10,20,30)
d4=demo(10,20,30,40)'''
#===========overriding in python======================================
'''class p:
    def properties_status(self):
        print("money, land, gold")
    def to_marry(self):
        print("xyz")
class C(p):
    def study_status(self):
        print("student done writing for job ")
    def to_marry(self):
        print("abc")
c=C()
c.properties_status()
c.to_marry()
c.study_status()
'''
'''class p:
    def properties_status(self):
        print("money, land, gold")
    def to_marry(self):
        print("xyz")
class C(p):
    def study_status(self):
        print("student done writing for job ")
    def to_marry(self):
        super().to_marry()
        print("abc")
c=C()
c.properties_status()
c.to_marry()
c.study_status()
'''
#================================
'''class person:
    def __init__(self, name , age):
        self.name=name
        self.age=age
class Employee(person):
    def __init__(self,  name, age ,eno , esal):
        super().__init__(name, age)
        self.eno=eno
        self.esal=esal
    def display(self):
        print("employee name:",self.name)
        print("employee age:",self.age)
        print("employee eno:",self.eno)
        print("employee salary:",self.esal)
e1=Employee("saumya",16,872425, 26000)
e1.display()
e2=Employee("Ranjith",20,735722, 36000)
e2.display()'''
#=====ABSTRACTION ==========================================
'''from abc import ABC, abstractmethod
#absteact class
class Bank(ABC):
    def bank_info(self):
        print("welcome to bank ")
    @abstractmethod
    def interest(self):
        "Abstract Method"  #if we remove these two statments error will generate
        pass
#sub class /child class of abstract class
class SBI(Bank):
    def interest(self):
        "Implementation of abstract method"
        print("In sbi bank 5 rupee interest")
s=SBI()
s.bank_info()
s.interest()'''
#========error will come======================================================================================
'''from abc import ABC, abstractmethod
#absteact class
class Bank(ABC):
    def bank_info(self):
        print("welcome to bank ")
    @abstractmethod
    def interest(self):
        "Abstract Method"
        pass
#sub class /child class of abstract class
class SBI(Bank):
    def balance(self):
        print("Balance is 100")
s=SBI()
s.bank_info()
s.balance()'''
#===using multilevel ==================================================
'''from abc import ABC ,abstractmethod
#abstract classs
class Bank(ABC):
    def bank_info(self):
        print("welcome to bank ")
    @abstractmethod
    def interest(self):
        "Abstract Method"
        pass
#sub class /child class of abstract class
class SBI(Bank):
    def balance(self):
        print("Balance is 100")
class sub1(SBI):
    def interest(self):
        print("In sbi bank 5 rupee interest")
s=sub1()
s.bank_info()
s.balance()
s.interest()'''
#=================================================================
from abc import ABC , abstractmethod
class Bank(ABC):
    def bank_info(self):
        print("welcome to bank ")
    @abstractmethod
    def interest(self):
        "Abstract Method"
        pass
    def offers(self):
        #remaining ====================


















