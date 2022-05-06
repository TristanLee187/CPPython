from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    s=rs()
    n=len(s)
    right=0
    leftzero=n-1
    for i in range(n):
        if s[i]=='1':
            right=i
        elif s[i]=='0' and leftzero==n-1:
            leftzero=i
    ans = max(1, leftzero - right + 1)
    print(ans)