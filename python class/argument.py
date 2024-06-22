#position argument
'''def sub(x,y):
    print(x-y)
sub(10,20)
#====error===================
def sub(x,y):
    print(x-y)
sub(10,20,30)'''
#===keyword argument
'''def details(id,name):
    print("emp id is:",id)
    print("emp name is:",name)
details(id=1,name="vandita")
details(id=2,name="preeti")'''
#======================
'''def details(id,name):
    print("emp id is:",id)
    print("emp name is:",name)
details(1,name="vandita")
#===error===================
def details(id,name):
    print("emp id is:",id)
    print("emp name is:",name)
details(name="vandita",1)'''
#===DEFAULT ARGUMENT========
'''def cart(item,price=20):
    print(item,"cost is :",price)
cart(item="pen")
cart(item="handbag",price=1000)
cart(price=500,item="shirt")
#=====error==================
def cart(item=1,price):
    print(item,"cost is :",price)
cart(item="pen")
cart(item="handbag",price=1000)
cart(price=500,item="shirt")'''
#=====VARIABLE LENGTH ARGUMENT=====================
'''def total_cost(x,*y):
    sum=0
    for i in y:
        sum+=i
    print(x+sum)
total_cost(100,200)
total_cost(110,226,311)
total_cost(11,)
#======ERROR=======
def total_cost(*y,x):
    sum=0
    for i in y:
        sum+=i
    print(x+sum)
total_cost(100,200)
total_cost(110,226,311)
total_cost(11,)
'''
#KEY VALUE PAIR===============
'''def m1(**x):
    for k ,v in x.items():
        print(k,"=",v)
m1(a=10,b=20,c=30)
m1(id=100,name="vandita")
'''









