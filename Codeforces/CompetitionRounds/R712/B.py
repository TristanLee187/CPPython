rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rs()
    b=rs()
    diffs=[]
    for i in range(n):
        if a[i]==b[i]:
            diffs.append(1)
        else:
            diffs.append(-1)
    poss=set()
    bal=0
    for i in range(n):
        if a[i]=='0':
            bal+=1
        else:
            bal-=1
        if bal==0:
            poss.add(i)

    curr=1
    ans=True
    for i in range(n-1,-1,-1):
        if diffs[i]*curr == -1:
            curr*=-1
            ans=ans and i in poss
    YN(ans)