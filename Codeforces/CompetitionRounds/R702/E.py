rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
def d(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=0
        d[i]+=1
    return d

for _ in range(rn()):
    n=rn()
    l=rl()
    a=[]
    for i in range(n):
        a.append([l[i],i+1])
    a.sort()
    l.sort()
    low=0
    high=n-1
    m=sum(l)
    ans=l[-1]
    while low<=high:
        mid=(low+high+1)//2
        num=a[mid][0]
        index=a[mid][1]
        og=num
        for i in a:
            if num>=i[0] and index!=i[1]:
                num+=i[0]
        if num==m:
            ans=min(ans,og)
            high=mid-1
        else:
            low=mid+1
    pans=[]
    for i in a:
        if i[0]>=ans:
            pans.append(i[1])
    print(len(pans))
    print(*sorted(pans))