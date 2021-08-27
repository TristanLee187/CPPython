from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,q=rns()
    s=rs()
    suff=[0 for i in range(n)]
    for i in range(n-1,-1,-1):
        suff[i]+=s[i]==['+','-'][i%2]
        if i!=n-1:
            suff[i]+=suff[i+1]
    suff.append(0)
    for __ in range(q):
        l,r=rns()
        # print(suff)
        l-=1
        mis=suff[l]-suff[r]
        diff=r-l
        if mis==diff/2:
            print(0)
        elif diff%2==1:
            print(1)
        else:
            print(2)
