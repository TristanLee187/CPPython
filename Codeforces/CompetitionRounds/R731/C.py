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
    k,n,m=rns()
    a=rl()
    a=a[::-1]
    b=rl()
    b=b[::-1]
    ans=[]
    while len(ans)<n+m:
        if len(a) and a[-1]==0:
            ans.append(a.pop())
        elif len(b) and b[-1]==0:
            ans.append(b.pop())
        elif len(a) and a[-1]<=k+len(ans):
            ans.append(a.pop())
            k-=1
        elif len(b) and b[-1]<=k+len(ans):
            ans.append(b.pop())
            k-=1
        else:
            ans=[-1]
            break
    print(*ans)