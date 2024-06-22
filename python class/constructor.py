
'''class employee:
    def __init__(self):
        print("constroctor:")
emp=employee()'''
#======================================================
'''class sample:
    def m1(self):
        print("m1 is instant method called with object name")
s=sample()
s.m1()
print(dir(sample))'''
#====default=====================
'''class employee:
    def __init__(self):
        print("constructor")
        print(self)
emp=employee()
emp1=employee()'''
#==================================================
'''class employee:
    def __init__(self):
       self.id=1
       print("employee id is:",self .id)
emp=employee()
emp1=employee()'''
#=====parameterized======================================
'''class employee:
    def __init__(self,id, name):
       self.id=id
       self.name=name
    def display(self):
        
       print("employee id is:",self .id)
       print("employee name is :",self.name)
emp=employee(1,"preeti")
emp.display()
emp1=employee(2,'kajal')
emp1.display()'''
#====area of triangle==================================
'''class rect:
   
    def __init__(self,b1,h1):
        self.l1=l1
        self.b1=b1
    def area(self):
        self.ar=l1*b1
        print("Area of rect is:",self.ar)

l1=int(input("enter the  length:"))
b1=int(input("enter the braedth:"))
r=rect(b1,l1)
r.area()
'''
#area of circle========================
'''class circle:
   
    def __init__(self,r):
       
        self.r=r
    def area(self):
        self.ar=3.14*(r**2)
        print("Area of circle is:",self.ar)

r=int(input("enter the  radius:"))
c=circle(r)
c.area()
'''
#=empployee details============================
'''class emp:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def display(self):
        print("name:",self.name)
        print("id:",self.id)
        print("salary:",self.salary)
name=input("enter the name of the employee:")
id=int(input("enter the id :"))
salary=int(input("enter the salary:"))
e=emp(name,id,salary)
e.display()'''

class emp:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def display(self):
        print("name:",self.name)
        print("id:",self.id)
        print("salary:",self.salary)
n=int(input("enter the no of employees you want to enter :"))
for i in range(1,n+1):
    name=input("enter the name of the employee:")
    id=int(input("enter the id :"))
    salary=int(input("enter the salary:"))
    e=emp(name,id,salary)
    e.display()












