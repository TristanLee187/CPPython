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
    i=a.index(min(a))
    j=a.index(max(a))
    poss=[max(i,j)+1, min(i,j)+1+(n-max(i,j)), n-min(i,j)]
    print(min(poss))