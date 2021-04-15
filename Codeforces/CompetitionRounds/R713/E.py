rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,l,r,s=rns()
    diff=r-l+1
    lo = diff*(diff+1)//2
    hi = lo+diff*(n-diff)
    if lo<=s<=hi:
        ans=list(range(n-diff+1,n+1))
        i=0
        sub=hi-s
        while sub>0:
            if ans[i]==i+1:
                i+=1
            else:
                ans[i]-=1
                sub-=1

        h=set(ans)
        pre=[]
        suff=[]
        for j in range(1,n+1):
            if j not in h:
                if len(pre)<l-1:
                    pre.append(j)
                else:
                    suff.append(j)
        print(*(pre+ans+suff))
    else:
        print(-1)