from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    ans=len(set(a))
    pans=[-1 for i in range(n)]
    s=set(range(1,n+1))
    ms=s.copy()
    gives=s.copy()
    for i in range(n):
        if a[i] in s:
            s.remove(a[i])

    for num in s:
        if a[num-1] in ms:
            gives.remove(num)
            ms.remove(a[num-1])
            pans[num-1]=a[num-1]

    for i in range(n):
        if a[i] in ms:
            gives.remove(i+1)
            pans[i]=a[i]
            ms.remove(a[i])

    gives=list(gives)
    ms=list(ms)

    if len(gives)>0:
        if gives[0]==ms[0]:
            gives[0],gives[1] = gives[1], gives[0]
        for i in range(len(gives)):
            if gives[i]!=ms[i]:
                pans[gives[i]-1]=ms[i]
            else:
                pans[gives[i-1]-1]=ms[i]
                pans[gives[i]-1]=ms[i-1]
                ms[i],ms[i-1]=ms[i-1],ms[i]

    print(ans)
    print(*pans)