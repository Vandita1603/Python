c=int(input("Enter your marks of c:"))
p=int(input("Enter your marks of p:"))
m=int(input("Enter your marks of m:"))
a=int(input("Enter your marks of a:"))
b=int(input("Enter your marks of b:"))
per=(c+p+m+a+b)/5
if per>=75:
    print("your grade is A")
elif per>=60:
    print("your grade is B")
elif per>=50:
    print("YOUR GRADE IS C")
elif per>=40:
    print("your grade is d")
else:
    print("you are fail")
