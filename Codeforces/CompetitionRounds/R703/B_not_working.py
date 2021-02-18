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
    l=[]
    for i in range(n):
        l.append(rl())
    l.sort()
    hor=[0]
    ver=[0]
    i=0
    for j in range(n):
        if i!=j:
            hor.append(l[j][0]-l[i][0])
            ver.append(l[j][1] - l[i][1])
    ans=1
    x=sum([abs(i) for i in hor])
    while True:
        for i in range(n):
            hor[i]-=1
        y=sum([abs(i) for i in hor])
        if y<x:
            ans=1
            x=y
        elif x==y:
            ans+=1
        else:
            break
    tans=ans
    y = sum([abs(i) for i in ver])
    while True:
        for i in range(n):
            ver[i] -= 1
        x = sum([abs(i) for i in ver])
        if x < y:
            ans = tans
            y = x
        elif x == y:
            ans += tans
        else:
            break
    print(ans)