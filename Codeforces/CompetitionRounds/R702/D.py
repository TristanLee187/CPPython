rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
def d(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=0
        d[i]+=1
    return d

for _ in range(rn()):
    n=rn()
    l=rl()
    ans=n*[0]
    def solve(arr,ans,add):
        if len(arr)==0:
            return 0
        ans[max(arr)-1]=add
        i=arr.index(max(arr))
        solve(arr[:i],ans,add+1)
        solve(arr[i+1:],ans,add+1)
    solve(l,ans,0)
    tans=[]
    for i in l:
        tans.append(ans[i-1])
    print(*tans)