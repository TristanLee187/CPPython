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
    a=[]
    curr=0
    last=s[0]
    for i in range(n):
        if s[i]==last:
            curr+=1
        else:
            a.append(curr)
            last=s[i]
            curr=1
    a.append(curr)
    oans=0
    for i in range(len(a)-1):
        if a[i]%2:
            oans+=1
            a[i+1]+=1
    print(oans)