#finding function
'''course="Python programming language"
print(course.find("p"))
print(course.find("a",1,20))'''
#=========substring using index meethod=============
'''s="Python programming language"
print(s.index("Python"))
'''
#=====exception handling======
'''s="Python programming language"
try:
    print(s.index("hello"))
    
except ValueError:
    print("not found")'''
#======count functiom=============
'''s="Python programming language ,Python is easy"
print(s.count("Python"))
print(s.count("hello"))'''
#======replace  function========
'''s1="Java programming language"
s2=s1.replace("Java","Python")
print(s1)
print(s2)
print(id(s1))
print(id(s2))

message="Python programming laguage"
n=message.split()
print("before spliting:",message)
print("after spliting:",n)
print(type(n))
for x in n:
    print(x)

message="Python programming laguage,Python is easy"
n=message.split(",")
print(n)
#==========join string ===============================
profile=['Roshan','Actor','India']
candidate='-'.join(profile)
print(profile)
print(candidate)
#==================CHAMGING CASES======================
message="Python programming laguage"
print(message.upper())
print(message.lower())
print(message.swapcase())
print(message.title())
print(message.capitalize())
#=================FORMAT FUNCTION=======================
name="Rakesh"
salary=100
age=16
print("{}'s salary is {} and his age is {}".format(name,salary,age))
print("{0}'s salary is {1} and his age is {2}".format(name,salary,age))
print("{x}'s salary is {y} and his age is {z}".format(x=name,y=salary,z=age))'''
#===================================================================================



















