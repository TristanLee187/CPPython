

for _ in range(int(input())):
    n=int(input())
    l=[]
    def dfs(s,last,limit,acc):
        a=2*last+s**2
        if a+acc<=limit:
            l.append(a)
            dfs(s+s,a,limit,acc+a)
            dfs(s+s+1,a,limit,acc+a)
    dfs(1,0,n,0)
    l.sort()
    ans=0
    s=0
    for i in range(len(l)):
        s+=l[i]
        if s<=n:
            ans+=1
    print(ans)
