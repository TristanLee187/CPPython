from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7


n,k,x=rns()
a=rl()
a.sort()
diff=[a[i]-a[i-1] for i in range(1,n)]
diff=sorted([i for i in diff if i>x])
ans=len(diff)+1
for d in diff:
    if k<=0:
        break
    cuts=d//x - int(d%x==0)
    k-=cuts
    if k>=0:
        ans-=1
print(ans)
