#==DECOR=====================================================================
'''def decor(func):
    def inner_function(x,y):
        if x<0:
            x=0
        if y<0:
            y=0
        return func(x,y)
    return inner_function

def add(a,b):
    res = a+b
    return res

add = decor(add)

print(add(20 ,30))
print(add(-10 , 5))'''
#======@SYMBOL========================================
'''def decor(func):
    def inner_function(x,y):
        if x<0:
            x=0
        if y<0:
            y=0
        return func(x,y)
    return inner_function
@decor
def add(a,b):
    res = a+b
    return res
print(add(20 ,30))
print(add(-10 , 5))
'''
#factorial===============================================
'''def decor(func):
    def inner_function(n):
        if n<0:
            print("the number is negetive")
        elif n==0:
            print("the value is : 1 or 0")
        else:
            return func(n)
    return inner_function

@decor
def fact(x):
    #x=int(input("enter the value :")
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
print("factorial is:",fact(5))
print("factorial is:",fact(-5))
'''
#======duck polimorphism========================================================
'''class Duck:
    def talk(self):
        print("Quack.......Quack")
class Dog:
    def talk (self):
        print("Bow.........Bow")

class Cat:
    def talk(self):
        print("meow.......Meow")
def m(obj):
    obj.talk()
duck=Duck()
m(duck)
cat=Cat()
m(cat)
dog=Dog()
m(dog)
'''
#=====operator overloading========================================
#print("#"*5, "="*10,"#"*5)
'''class Book:
    def __init__(self,pages):
        self.pages=pages
b1=Book(100)
b2=Book(200)
print(type(b1))
print(type(b2))
print(type(b1.pages))
print(type(b2.pages))
print(b1.pages+b2.pages)
print((b1.pages).__add__(b2.pages))
'''
#===============================================================
'''class Book:
    def  __init__(self,pages):
        self.pages=pages
    def __add__(self,others):
        return self.pages + others.pages
b1=Book(100)
b2=Book(200)
print(b1 + b2)'''
#=====magic method===================================================
'''class student:
    def __init__(self, name ,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __lt__(self,other):
        return self.marks<other.marks
s1=student("Samvida", 100)
s2=student("Surya",200)
print("s1>s2=",s1>s2)
print("s1<s2=",s1<s2)
#print("s1>=s2=",s1>=s2)         #>,<sign is not aplicable in this we can overload by magicn methods
#print("s1<=s2=",s1<=s2)
'''
#====overloading============================================================
'''class demo:
    def m1(self):
        print("no argument method")
    def m1(self,a):
        print(" one argument method")
    def m1(self,a,b):
        print("tow argument method")
d=demo()
d.m1()
d.m1(2)
d.m1(10,20)'''
#============================================
class demo:
    def sum(self, a=None,b=None,c=None):
        if a!=None and b!= None  and c!=None:
            print("the sum of 3 numbers:",a+b+c)
        elif a!=None and b!= None:
            print("the sum of 3 numbers:",a+b)
        else:
            print("please provide 2 or 3 arguments")
d=demo()
d.sum(10,20,30)
d.sum(10,20)
d.sum(10)





















