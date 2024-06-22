#=====indexing of string=============
"""wish="hello world"
print(wish[0])
print(wish[-1])
print(wish[-2])
print()"""
#====================================
"""name="python"
for a in name:
    print(a)"""
#==========SLICING===================
'''wish="hello world"
print(wish[::])
print(wish[:])
print(wish[0:9:1])
print(wish[0:9:2])
print(wish[2:4:1])
print(wish[::2])
print(wish[2::])
print(wish[:4:])'''
#=====replacement not allowed=======
'''name="vandita"
print(name)
print(name[0])
name[0]="x"
'''
#======addition & multiplication=====
'''n1="vandita"
n2=" bharti"
print(n1+n2)
print(n1*2)'''
#===len function====================
'''n1="vandita"
print("length is :",len(n1))
print("Avalibility of chracters")
print('v' in 'vandita')
print('p' in 'vandita')'''
#==========================
'''main=input("Enter your string")
s=input("Enter substring")
if s in main:
    print(s,"is found in main string")
else:
    print(s,"is not found in main string")'''
#==========================
'''s1="abcd"
s2="abcdefg"
print(s1==s2)
if (s1==s2):
    print("both are same")
else:
    print("both are not same")'''

#=====user name validation====
'''user="rahul"
name=input("enter your user name")
if user==name:
    print("welcome to gmail:",name)
else:
    print("invalid user name")'''
#=====remove space========
'''course="    python"
print("with space course length is :",len(course))
x=course.strip()
print("after removing space, course length is:",len(x))
x=course.rstrip()
print("after removing space, course length is:",len(x))
x=course.lstrip()
print("after removing space, course length is:",len(x))'''
#=========find function======
'''course="Python programming language"
print(course.find("p"))
print(course.find("a",1,20))
'''
#==================
s="Python programming language"
print(s.index("Python"))

#=====exception handling======
s="Python programming language"
try:
    print(s.index("hello"))
    
except ValueError:
    print("not found")


















