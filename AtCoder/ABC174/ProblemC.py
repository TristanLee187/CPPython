k=int(input())
if k%2==0 or k%5==0:
    print(-1)
elif k==7:
    print(1)
else:
    i=1
    num=1
    if k%7==0:
        k=k//7
    while num%k!=0:
        i+=1
        num=10*num+1
    print(i)
    
    
    
    
    
    
    
