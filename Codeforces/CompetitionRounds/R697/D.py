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
    n,m=rns()
    a=rl()
    b=rl()
    if sum(a)<m:
        print(-1)
    else:
        ones=[]
        twos=[]
        for i in range(n):
            if b[i]==1:
                ones.append(a[i])
            else:
                twos.append(a[i])
        ones.sort(reverse=True)
        twos.sort(reverse=True)
        i=0
        j=0
        acc=0
        while acc<m and i<len(ones):
            acc+=ones[i]
            i+=1
        while acc<m and j<len(twos):
            acc+=twos[j]
            j+=1
        ans=i+2*j
        while i>0:
            i-=1
            acc-=ones[i]
            while acc<m and j<len(twos):
                acc+=twos[j]
                j+=1
            if acc>=m:
                ans=min(ans,i+2*j)
        print(ans)