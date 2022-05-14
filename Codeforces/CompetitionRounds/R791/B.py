from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7


n,q=rns()
nums=rl()
ans=sum(nums)
flag=False
indeces= {}
flagnum=-1
for i in range(q):
    query = rl()
    if query[0]==1:
        a,x=query[1:]
        if flag and a-1 in indeces:
            ans-=indeces[a-1]
            ans+=x
            indeces[a-1]=x
        elif flag:
            ans-=flagnum
            ans+=x
            indeces[a-1] = x
        else:
            ans-=nums[a-1]
            nums[a-1]=x
            ans+=x
    else:
        x=query[1]
        flagnum=x
        ans=n*x
        indeces.clear()
        flag=True
    print(ans)
