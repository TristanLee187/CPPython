from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    a,b=rns()
    diff=b-a
    ans=0
    for i in range(len(str(a+diff))):
        ans+=(a+diff)//(10**i) - a//(10**i)
    print(ans)