from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,d=rns()
    a=rl()
    loops=[]
    seen=set()
    ans=0
    for i in range(n):
        if i in seen:
            break
        seen.add(i)
        loop=[a[i]]
        j=(i-d)%n
        while j!=i:
            seen.add(j)
            loop.append(a[j])
            j=(j-d)%n
        loops.append(loop)

    for loop in loops:
        if 0 not in loop:
            ans=-1
            break
        i=loop.index(0)
        loop = loop[i:]+loop[:i]
        curr=0
        for i in range(1,len(loop)):
            if loop[i]==1:
                curr+=1
            else:
                curr=0
            ans=max(ans,curr)
    print(ans)
