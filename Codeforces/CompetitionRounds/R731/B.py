from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    s=rs()
    a=[(ord(s[i]),i) for i in range(len(s))]
    a.sort()
    ans=a[0][0]==97
    l=a[0][1]
    r=a[0][1]
    for i in range(1,len(s)):
        if a[i][0] != a[i-1][0]+1:
            ans=False
        elif a[i][1]==r+1:
            r+=1
        elif a[i][1]==l-1:
            l-=1
        else:
            ans=False
    YN(ans)