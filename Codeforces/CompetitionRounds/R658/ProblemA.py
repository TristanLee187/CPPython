t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    buckets={}
    for i in a:
        if i in buckets:
            buckets[i]+=1
        else:
            buckets[i]=1

    found=False
    ans=0
    for i in b:
        if i in buckets:
            ans=i
            found=True
            break

    if found:
        print('YES')
        print(1, ans)
    else:
        print('NO')
            
    
    
