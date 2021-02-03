t = int(input())
count=0
while count<t:
    count+=1
    x = int(input())
    temp=x
    ans=0
    take=2
    while temp>1:
        while temp-take>=0:
            temp-=take
            take+=3
        ans+=1
        take=2
    print(ans)
    
