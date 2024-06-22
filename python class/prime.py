num=int(input("enter a number"))
count=0
x=1
while x<=num:
    if num%x==0:
        count+=1
    x+=1
if count==2:
    print("number is a prime")
else:
    print("number is not prime")
