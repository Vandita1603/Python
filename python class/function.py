#===========function ======================
'''def  display():
    print("welcome to function")
display()
display()
display()'''
#========error on this code ===================
'''def one():
    print("vsuybsuj")
two()
'''
#=====function without parameters=================
'''def add():
    a=int(input("enter number :"))
    b=int(input("enter number :"))
    c=a+b
    print("addition:=",c)
add()
def add(a,b):
    c=a+b
    print("addition:=",c)
a=int(input("enter number :"))
b=int(input("enter number :"))
add(a,b)'''

#==========factorial=======================

def fact(n):
    f=1
    if n<0:
        print("negetive number")
    elif n==0:
        print("factorial is 1")
    else :
        for i in range(1,n+1):
            f=f*i
        print("factorial :",f)
for x in range(1,6):
    n=int(input("enter a number:"))
    fact(n)












