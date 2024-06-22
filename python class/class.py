'''class demo:
    name= "vandita"
    roll= 101
obj=demo()
print("my name is :",obj.name)
print("my roll no is:",obj.roll)'''
#=====user defined==================================
'''class user:
    name=None
    roll=0
obj=user()
obj.name=input("enter the name ")
obj.roll=int(input("enter the roll no."))
print("my name is :",obj.name)
print("my roll no is:",obj.roll)'''
#=============================
'''class user:
    name=None
    roll=0
    grade=None
obj=user()
obj.name=input("enter the name ")
obj.roll=int(input("enter the roll no."))
obj.grade=input("enter the grade:")

print("my name is :",obj.name)
print("my roll no is:",obj.roll)
print("my grade is:",obj.grade)'''
#======function=====================
'''class demo:
    def display(self):
        print("hello this is display method")
obj=demo()
obj.display()'''
#==========================================
'''class details:
    name,grade=None,None
    roll=0
    per=0.0
    
    def get_data(self):
        
        self.name=input("enter the name :")
        self.roll=int(input("enter the roll:"))
        self.per=float(input("enter the per:"))
        self.grade=input("enter the grade:")
    def put_data(self):
        print("name:",self.name)
        print("roll no.:",self.roll)
        print("per:",self.per)
        print("garde:",self.grade)
obj=details()
obj.get_data()
obj.put_data()'''
#===============================================
'''class details:
    def display(self,name,roll,per,grade):
        print("name:",name)
        print("roll no.:",roll)
        print("per:",per)
        print("garde:",grade)
obj=details()
obj.display("vandita",73,81,"A")'''
#=================================================
'''class student:
    name,grade=None,None
    roll=0
    per=0.0
    def display(self,n,r,p,g):
        self.name=n
        self.roll=r
        self.per=p
        self.grade=g
        print("name:",self.name)
        print("roll no.:",self.roll)
        print("per:",self.per)
        print("garde:",self.grade)
obj=student()
obj.display("vandita",73,81.0,"A")'''
#==================================================================
class student:
    name,grade=None,None
    roll=0
    per=0.0
    def display(self,n,r,p,g):
        self.name=n
        self.roll=r
        self.per=p
        self.grade=g
        print("***************Student details are*****************")
        print("name:",self.name)
        print("roll no.:",self.roll)
        print("per:",self.per)
        print("garde:",self.grade)
obj=student()
n=input("enter the name :")
r=int(input("enter the roll:"))
p=float(input("enter the per:"))
g=input("enter the grade:")
obj.display(n,r,p,g)










