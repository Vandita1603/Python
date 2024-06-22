#=====SET===================
'''s={10,20,30,40}
print(s)
print(type(s))'''
#===SET WITH DIFFERENT ELEMENT=================
'''s={10,'20','Rahul',234.56,True}
print(s)
print(type(s))'''
#============RANGE()========================
'''s=set(range(5))
print(s)'''
#=====DUPLICTE NOT ALLOWED=================
'''a={10,20,30,40,10,10}
print(a)
print(type(a))'''
#==========SET()==================================
'''r=range(0,10)
s=set(r)
print(s)
print(type(s))'''
#=====EMPTY SET===========================
'''d={}
print(d)
print(type(d))
s=set()
print(s)
print(type(s))'''
#========ADD()=====================
'''S={10,20,30}
S.add(40)
print(S)'''
#======UPDATE()=====================
'''s={10,20,30}
l=[40,50,60,10]
s.update(l)
print(s)'''
#=============================
'''s={10,20,30,40}
l=[40,50,60,10]
s.update(l,range(5))
print(s)'''
#================================
'''s={20,30,40}
s.add(10)
print(s)
#s.add(10,20,30)    #invalid
#s.update(10)     #invalid
s.update(range(1,10,2),range(0,10,2))
print(s)'''
#=======cvopy()==================
'''p={10,20,30}
p1=p.copy()
print(p1)'''
#=========pop()====================
'''s={40,10,30,20}
print(s)
print(s.pop())
print(s)'''
#======REMOVE()==================
'''s={40,10,30,20}
s.remove(30)
#s.remove(50)  #invalid
print(s)'''
#======DISCARD()==================
'''s={10,20,30}
s.discard(10)
print(s)
s.discard(50)
print(s)'''
#=CLEAR()=====================================
'''s={10,20,30}
print(s)
s.clear()
print(s)'''
#=====UNION()============================
'''x={10,20,30,40}
y={30,40,50,60}
print(x.union(y))
#========intersection============
print(x.intersection(y))
print(x&y)'''
#difference========================
'''x={10,20,30,40}
y={30,40,50,60}
print(x.difference(y))
print(x-y)
print(y-x)'''
#symmetric--------------------------
'''x={10,20,30,40}
y={30,40,50,60}
print(x.symmetric_difference(y))
print(x^y)'''
#======frozenset()==============
v=('a','e','i','o','u')
f=frozenset(v)
print(f)
print(type(f))






















