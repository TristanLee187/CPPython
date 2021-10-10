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
    a=[rl() for _ in range(n)]
    ans=False
    for i in range(5):
        for j in range(5):
            if i!=j:
                first=0
                second=0
                both=0
                for k in range(n):
                    if a[k][i] and a[k][j]:
                        both+=1
                    elif a[k][i]:
                        first+=1
                    elif a[k][j]:
                        second+=1
                    else:
                        break
                if first+second+both==n and first<=n//2 and second<=n//2:
                    ans=True
                    break
    YN(ans)
