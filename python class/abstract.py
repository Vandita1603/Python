'''from abc import ABC, abstractmethod
class One(ABC):
    @abstractmethod
    def calculate(self ,a):
        pass
    def m1(self):
        print("implemented method")
class Square(One):
    def calculate(self, a):
        print("Square:", a )
class Cube(One):
    def calculate(self, a):
        print("cube:",(a*a*a))
s=Square()
c=Cube()
s.calculate(2)
c.calculate(2)'''
#========================================================================================
'''from abc import *
class demo(ABC):
    def m(Self):
        print("calling")
d=demo()
d.m()'''
#===================================================================
from abc import *
class demo:
    @abstractmethod
    def m(self):
        pass
    def n(self)























