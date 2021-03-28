rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')

for _ in range(rn()):
    n,q=rns()
    l=rl()
    ans=max(l)
    tans=0
    le=float('inf')
    r=-1
    for i in range(n):
        if i==0:
            if n>1 and l[i]>l[i+1]:
                tans+=l[i]
                le=min(le,i)
                r=max(r,i)
        elif i==n-1:
            if n>1 and l[i]>l[i-1]:
                tans+=l[i]
                le = min(le, i)
                r = max(r, i)
        else:
            if l[i]>l[i-1] and l[i]>l[i+1]:
                tans+=l[i]
                le = min(le, i)
                r = max(r, i)
    for i in range(n):
        if i>le and i<r and l[i]<l[i-1] and l[i]<l[i+1]:
            tans-=l[i]

    print(max(ans,tans))