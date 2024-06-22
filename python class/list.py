'''l=[]
print(l)
print(type(l))
name=["mohan","prasaed","ramesh",10,20,True,None]
print(name)
print()'''
#===============list() function===================================
'''r=range(0,10)
l=list(r)
print(l)
print()'''
#==================MUTABILITY=========================
'''P=[1,2,3,4,5]
print(P)
print("before modifing p[0]:",P[0])
P[0]=20
print("After modifing p[0]:",P[0])
print(P)
print()'''
#==================LIST INDEXING=========================
'''name=["prabhas","prashant","prakash"]
print(name)
print(name[0])
print(name[1])
print(name[2])
print(type(name))
print(type(name[0]))
print(type(name[1]))
print(type(name[2]))
print()'''
#=========LIST INDEXING out of range error=========================
'''name=["prabhas","prashant","prakash"]
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[10])'''
#===============SLICING==================================
'''n=[1,2,3,4,5,6]
print(n)
print(n[2:5:2])
print(n[4::2])
print(n[3:5])'''

#===============USING LOOP(FOR)==================
'''a=[100,200,300,400]
for x in a:
    print(x)
print()'''
#=================WHILE=========================
'''a=[100,200,300,400]
x=0
while x<len(a):
    print(a[x])
    x=x+1
'''
#===============len() method=================
'''n=[1,2,3,4,5]
print(len(n))'''
#================count() method===================
'''n=[1,2,3,4,5,5,5,3]
print(n.count(5))
print(n.count(3))
print(n.count(2))'''
#===============append() method===================
'''l=[]
l.append("Ramesh")
l.append("Suresh")
l.append("naresh")
print(l)'''
#================insert() method======================
'''n=[10,20,30,40]
n.insert(0,76)
print(n)
print()
l=[10,20,30,40]
print(l)
l.insert(1,111)
print(l)'''
#============extend()==================================
'''l1=[1,2,3]
l2=['rahul','Rakesh','Ragina']
print('before extend l1 is:',l1)
print('before extend l2 is:',l2) 
l2.extend(l1)
print('After extend l1 is:',l1)
print('After extend l2 is:',l2) '''
#==================================
'''august_txns=[100,200,300,400,500,900]
sept_txns=[111,222,333,600,790,100,200]
print("August month transaction are:",august_txns)
print("september month transaction are:",sept_txns)
sept_txns.extend(august_txns)
print("August and sept total transaction amount:",sum(sept_txns))'''
#=================REMOVE()====================================
'''n=[1,2,3,1]
n.remove(1)
print(n)'''
#=====================ERROR======================
'''n=[1,2,3,1]
n.remove(10)
print(n)'''
#=====================POP()====================
'''n=[1,2,3,4,5]
print(n.pop(1))
print(n)
print(n.pop())
print(n)'''
#==================REVERSE()====================
'''n=[1,2,3,4,'two']
print(n)
n.reverse()
print(n)'''
#======================SORT()========================
'''n=[1,4,5,3,2]
n.sort()
print(n)
s=['Suresh','Ramesh','Arjun']
s.sort()
print(s)'''
#=================ALIASING=============================
'''x=[10,20,30]
y=x
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))
print()'''
#=========CLONING USING SLICING OP========================
'''x=[10,20,30]
y=x[:]
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))
'''
#=========CLONING USING COPY() METHOD===============
'''x=[10,20,30]
y=x.copy()
print(x)
print(y)
print(id(x))
print(id(y))
'''
#==========MATHEMATICAL OPERATOR===================
#===========CONCATENATION============================
'''a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)'''
#=========ERROR-=====================================
'''a=[1,2,3]
b='Balu'
c=a+b
print(c)'''
#==============MULTIPLICATION=======================
'''a=[1,2,3]
print(a)
print(a*2)'''
#=========COMPARISION===============================
'''print([1,2,3]<[1,2,3])
print([1,2,3]<[2,2,3])
print([1,2,3]<=[1,2,3])
print([1,2,3]<[1,2,4])
print([1,2,3]<[0,2,3])
print([1,2,3]==[1,2,3])
'''
#=========string comp========================
'''x=["abc","def","ghi"]
y=["abc","def","ghi"]
z=["ABC","DEF","GHI"]
a=["abc","def","ghi","jkl"]
print(x==y)
print(x==z)
print(x==a)'''
#===========MEMBERSHIP OP========================
'''x=[10,20,30,40,50]
print(20 in x)
print(20 not in x)
print(90 in x)
print(90 not in x)'''
#===========NESTED LIST==============================
'''a=[80,90]
b=[10,20,30,a]
print(b[0])
print(b[1])
print(b[2])
print(b[3])'''
#=========MULTIPLYING========================
'''x=[1,2,3,4]
y=[]
for i in x:
    y.append(i*2)
print(y)'''
#========LIST COMPREHENSIONS=============
'''X=[1,2,3,4]
y=[i*2 for i in X]
print(y)''''
#===================
s=range(1,20,3)
for i in s:
    print(i)
m=[x for x in s if x%2==0]
print(m)










