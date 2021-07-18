from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    input()
    a,A=rns()
    b,B=rns()
    f,F=rns()
    ans=abs(a-b)+abs(A-B)
    if a==b and A==B:
        pass
    elif a==b==f:
        l,r=sorted([A,B])
        if l<=F<=r:
            ans+=2
    elif A==B==F:
        l, r = sorted([a, b])
        if l <= f <= r:
            ans += 2
    else:
        pass
    print(ans)