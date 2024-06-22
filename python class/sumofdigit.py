#sum of digit
'''num=int(input("enter a number"))
val=0
while num>0:
    rem=num%10
    val=val+rem
    num=num//10
print("sum of digit is :",val)'''
#product of digit
num=int(input("enter your num "))
p=1
while num>0:
    rem=num%10
    p=p*rem
    num=num//10
print("product of digit is :",p)
