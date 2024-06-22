#ARMSTRONG NUMBER
num=int(input("enter a number"))
sum=0
val=num
dig=len(str(num))
while num>0:
    rem=num%10
    p=rem**dig
    sum=sum+p
    num=num//10
if num==val:
    print("armstrong number",sum) 
else:
    print("number is not armstrong",sum)
