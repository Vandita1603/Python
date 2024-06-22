#palindrome
num=int(input("enter a number"))
sum=0
val=num

while num>0:
    rem=num%10
    sum=sum*10+rem
    num=num//10
if num==val:
    print("palindrome number:",sum) 
else:
    print("number is not armstrong:",sum)






























    
