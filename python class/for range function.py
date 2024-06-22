'''for x in range(1,5):
    print(x)
'''
#find odd
'''print("Odd numbers in this range are:")
for x in range(1,11):
    if x%2!=0:
        print(x)'''
#table of any no.
#fabionici series
'''num=int(input("enter any number:"))
a=-1
b=1
for i in range(0,num+1):
    c=a+b
    print(c)
    a=b
    b=c'''
#sum 
'''sum=0
for i in range(1,10):
    print(i)

    sum=sum+i
    
print("sum of range values:",sum)'''
#sum of digit
'''num=int(input("enter a digit:"))
sum=0
for i in range(0,num+1):
    rem=num%10  
    sum=sum+rem
    num=num//10
print("sum of range values:",sum)'''
#2 method
num=int(input("enter a digit:"))
sum=0
d=len(str(num))
for i in range(d):
    
    rem=num%10  
    sum=sum+ int(i)
    num=num//10
print("sum of range values:",sum) 








        
