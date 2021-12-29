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
    n=rn()
    s=rs()
    ans=s[0]
    for i in range(1,n):
        if s[i]<s[i-1] or (s[i]==s[i-1] and s[i]!=ans[0]):
            ans+=s[i]
        else:
            break
    print(ans+ans[::-1])