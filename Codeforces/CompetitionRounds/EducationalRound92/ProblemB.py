import bisect
import math

t=int(input())
for _ in range(t):
    n,k,z=map(int,input().split())
    l=list(map(int,input().split()))
    l=l[:k+1]
    n=len(l)

    sums=[]
    for i in range(n-1):
        sums.append(l[i]+l[i+1])
    indexes=list(range(n-1))

    tsums=[]
    tindexes=[]

    for i in range(n-1):
        j=bisect.bisect_left(tsums,sums[i])
        tsums.insert(j,sums[i])
        tindexes.insert(j,i)

    tsums=tsums[::-1]
    tindexes=tindexes[::-1]
    times=[]
    for i in range(n-1):
        times.append(math.ceil((n-(tindexes[i]+2))/2))

    ans=0
    i=0
    print(tsums)
    print(tindexes)
    print(times)
    while i<n:
        if i<tindexes[0]+2 or z==0:
            ans+=l[i]
            i+=1
        else:
            ans+=min(z,times[0])*tsums[0]
            n-=min(z,times[0])*2
            z-=min(z,times[0])
            times.pop(0)
            tsums.pop(0)
            tindexes.pop(0)
    print(ans)
            
        
        
    
        

    
    
    
    
        
        
        
    
