from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    x=rn()
    a=[int(i) for i in str(x)]
    ans=True
    if len(a)==1:
        ans=False
    elif len(a)==2:
        ans=x%11==0
    else:
        for i in range(1,len(a)-1):
            if i==len(a)-2 and a[i]<a[i+1]:
                ans=False
            if a[i]<a[i-1] and a[i]<a[i+1]:
                ans=False
    YN(ans)
