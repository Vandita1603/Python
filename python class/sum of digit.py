num=int(input("enter a number :"))
val=0
x=0
while x<=num:
    rem=num%10
    val=val+rem
    num=num/10
    print(val)
