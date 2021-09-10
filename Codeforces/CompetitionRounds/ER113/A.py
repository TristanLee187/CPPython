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
    s=rs()
    if len(set(s))==1:
        print(-1,-1)
    else:
        for i in range(n-1):
            if s[i]!=s[i+1]:
                print(i+1,i+2)
                break