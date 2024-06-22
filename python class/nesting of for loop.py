#nesting of loop
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()
# *
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
for i in range(1,6):
    for j in range(1,i+1):
        
        print("*",end=" ")
    
    print()
print()
#======================================
for i in range(1,6):
    for j in range(1,7-i):
        
        print("*",end=" ")

    print()
#======================================
for i in range(1,6):
    for j in range(1,i+1):
        
        print(j,end=" ")
    
    print()
print()
#======================================
for i in range(1,6):
    for j in range(1,i+1):
        
        print(i,end=" ")
    
    print()
print()
#======================================
for i in range(1,6):
    for j in range(1,i+1):
        c=i+j
        if c%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    
    print()
print()
#======================================
for i in range(1,6):
    
    for j in range(1,6-i):
        
        print(" ",end=" ")
    for j in range(1,i+1):
        
        print("*  ",end=" ")
    print()
    i=i+1
print()
#======================================
for i in range(1,6):
    
    for j in range(1,6-i):
        
        print(" ",end=" ")
    for j in range(1,i+1):
        
        print("*",end=" ")
    print()
    i=i+1
print()
#======================================
for i in range(1,6):
    
    for j in range(1,6-i):
        
        print(" ",end=" ")
        j=j+1
        p=i
    for j in range(1,i+1):
        
        print(p,end=" ")
        p=p+1
        j=j+1
    p=p-2
    for j in range(1,i):
        
        print(p,end=" ")
        p=p-1
        j=j+1
    
    print()
    i=i+1
print()
#======================================
for i in range(1,6):
    
    for j in range(1,6-i):
        
        print(" ",end=" ")
    for j in range(0,2*i-1):
        
        print("*",end=" ")
    print()
    i=i+1
print()


