from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n=rn()
items=[rl()[1:] for _ in range(n)]
m=rn()
banned={tuple(rns()) for _ in range(m)}