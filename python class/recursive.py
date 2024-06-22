#RECURSIVE FUNCTION
'''def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
x=fact(4)
print("factorial of  4 is:",x)'''
#sum of digit
def  dig(n):
    if n==0:
        return- 0
    else:
        return (n%10+dig(int(n//10)))

x=int(input("enter a num:"))
result=dig(x)
print("sum of  digit is:",result)
