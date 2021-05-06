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
    s=rs()
    h=set()
    ans=True
    for i in range(n):
        if s[i] in h and i>0 and s[i]!=s[i-1]:
            ans=False
        h.add(s[i])
    YN(ans)