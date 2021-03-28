rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')

for _ in range(rn()):
    n,t=rns()
    l=rl()
    for i in range(n):
        l[i]=[l[i],i]
    l.sort()
    ans=n*[0]
    ans[l[0][1]]=1
    i=1
    while i<n and l[i-1][0]<t-l[i][0] and l[i][0]!=t/2:
        ans[l[i][1]]=1
        i+=1
    c=0
    j=float('inf')
    for i in range(n):
        if l[i][0]==t/2:
            j=min(j,i)
            c+=1
    if c!=0:
        for k in range(int(j),int(j)+c//2):
            ans[l[k][1]]=1
    print(' '.join(list(map(str,ans))))



