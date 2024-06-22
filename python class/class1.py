emp_id = 11
r_no=61
nm="vandita"
per=82.8
grd='a'
print("employe id is ",emp_id)
print("roll no is:",r_no)
print('name of student:',nm)
print("percentage is:",per,"%")
print("grade is:",grd)
print()
#================TYPE======================
print("type of employee id -",type(emp_id))
print("type of roll no.-",type(r_no))
print("type of name-",type(nm))
print("type of percentage-",type(per))
print("type of grade-",type(grd))
print()
#=====MULTIPLE IDENTIFERS==========
A,B,C=2,4,6
print(A,B,C)
print()
#=======RE-INITIALIZATION===========
V=3
print("Before re-initialization:",V)
V=4
print("After re-initialization:",V)
print()
#=======PRINT FLOAT VALUES==========
s=2e2
p=2E2
k=2e3
print("float value of s is:",s)
print("float value of p is:",p)
print("float value of k is:",k)
print(type(s))
print()
#=======COMPLEX VALUES==============
r=3+5j
w=2-5.5j
i=3+10.5j
print("complex value of r:",r)
print("complex value of w:",w)
print("complex value of i:",i)
print("type of w:",type(w))
print()
print("addition :",r+w)
print("substract:",w-i)
print()
#========BOOLEAN VALUES==============
u=True
y=False
print("value of u:",u)
print("value of y:",y)
print("add u:",u+u)
print("add u and y:",u+y)
#========USING NONE==================
n=None
print(n)
print(type(n))
#=========STRING DATATYPE===========
name1="vandita"
name2="""vandita"""
print(name1," ",name2)
#==========BYTE DATATYPE============
x=[10,20,30,40,50]
q=bytes(x)
print(type(q))
#----------INDEX VALUE-------------
print(q[0])
print(q[1])
print(q[2])
print(q[3])
print(q[4])
#=======BYTEARRAY================
Q=[3,4,5,6,7]
Y=bytearray(Q)
print(Y)
print(type(Y))



