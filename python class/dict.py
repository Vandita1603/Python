'''d={1:"ramesh",2:"suresh",3:"vandita"}
print(d)'''
#==emptuy================
'''d={}
d[1]="prashant"
d[2]="saumya"
d[3]="vandita"
print(d)'''
#==================
'''d={1:"ramesh",2:"suresh",3:"vandita"}
print(d[1])
print(d[2])
print(d[3])'''
#handle the key error=================
'''d={1:"ramesh",2:"suresh",3:"vandita"}
if 400 in  d:
    print(d[400])
else:
    print("wrong key input")'''
#===employee details user input==========
'''d={}
n=int(input("Enter number of employess:"))
i=1
while i<=n:
    name=input("Enter the name of the employee:")
    salary=int(input("Enter the salary of the employee:"))
    d[name]=salary
    i=i+1
for x in d:
    print("The  name is:",x,"and salary is:S",d[x])'''
#replace or adding the value============
'''d={1:"ramesh",2:"suresh",3:"vandita"}
print("old dictionary:",d)
d[10]="saumya"
print("adding a new key and value:",d)
d[2]="preeti"
print("replacing the value in the existing one:",d)'''
#deleting the key and value====================
'''d={1:"ramesh",2:"suresh",3:"vandita"}
print("before deleting the key :",d)
del d[1]
print("after deleting the key from dictionary:",d)'''
#ERROR=======================================
'''d={1:"ramesh",2:"suresh",3:"vandita"}
print("before deleting the key :",d)
del d[10]
print("after deleting the key from dictionary:",d)'''
#CLEAR=================================
'''d={1:"ramesh",2:"suresh",3:"vandita"}
print("before clearing  the key :",d)
del d
#print("after  the key from dictionary:",d)        #AFTER clearing it will give an error
'''
#======DICT() FUNCTION==================
'''d=dict()
print(d)
print(type(d))
d=dict({1:"ramesh",2:"suresh",3:"vandita"})
print(d)
'''
#=====tuple form=========
'''d=dict([(1,"vandita"),(2,"preeti")])
print(d)'''
#==========get()=============
'''d={1:"ramesh",2:"suresh",3:"vandita"}
print(d.get(1))
print(d.get(100,'no key found'))'''
#======pop()======================
'''d={1:"ramesh",2:"suresh",3:"vandita"}
print("befor",d)
d.pop(1)
print(d)'''
#======popitem()==============
'''d={1:"ramesh",2:"suresh",3:"vandita"}
print("befor",d)
d.popitem()
print(d)'''
#====error=====================
'''d={}
d.popitem()
print(d)'''
#====key()======================
'''d={1:"ramesh",2:"suresh",3:"vandita"}
print(d)
for k in d.keys():
    print(k)'''
#===values===========================
''''d={1:"ramesh",2:"suresh",3:"vandita"}
print(d)
for k in d.values():
    print(k)'''
#=====items===============
''''d={1:"ramesh",2:"suresh",3:"vandita"}
print(d)
for k ,v in d.items():
    print(k,"------->",v)'''
#=======copy()=======================
'''d1={1:"ramesh",2:"suresh",3:"vandita"}
d2=d1.copy()
print(d1)
print(d2)'''
#==========square()====================
d={a:a*a for a in range(1,6)}
print(d)








    
