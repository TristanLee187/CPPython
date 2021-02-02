rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(int(input())):
    ans = 0
    n=rn()
    l=rl()
    lans=[0]
    def dfs(a,n,acc):
        def merge(a,n):
            s=a[n]+a[n+1]
            a[n]=s
            a.pop(n+1)
            return s
        s=merge(a,n)
        for i in range(len(a)-1):
            b=a.copy()
            dfs(b,i,acc+s)
        if len(a)==1:
            lans[-1]+=acc+s
    for i in range(n-1):
        a=l.copy()
        dfs(a,i,0)
    def fact(n):
        ans=1
        for i in range(2,n+1):
            ans*=i
        return ans
    ans=lans[0]/fact(n-1)
    print('Case #' + str(_ + 1) + ': ' + str(ans))
