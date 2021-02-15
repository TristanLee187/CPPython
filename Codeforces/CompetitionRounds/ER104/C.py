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
    c=(n-1)//2
    ans=[]
    for i in range(1,n):
        for j in range(i+1,n+1):
            if j-i<n/2:
                ans.append(1)
            elif j-i==n/2:
                ans.append(0)
            else:
                ans.append(-1)
    print(*ans)