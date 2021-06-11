from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    avg=sum(a)/n
    if int(avg)!=avg:
        print(-1)
    else:
        s=0
        ans=0
        for i in a:
            if i<avg:
                s+=abs(i-avg)
        a.sort()
        while a[-1]>avg:
            ans+=1
            s-=a.pop()
        while s>0:
            ans+=1
            s-=a.pop()
        print(ans)