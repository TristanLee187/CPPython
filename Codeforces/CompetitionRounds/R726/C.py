from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    a.sort()
    nums=[-1,-1]
    diff=float('inf')
    flag=False
    c,d=-1,-1
    if a.count(a[0])>1:
        nums=[a[0],a[0]]
    elif a.count(a[-1])>1:
        nums=[a[-1],a[-1]]
    else:
        for i in range(n-1):
            cdiff=a[i+1]-a[i]
            if cdiff<diff:
                diff=cdiff
                flag=True
                c,d=i,i+1
    if n==2:
        ans=a
    elif flag:
        ans=a[c+1:]+a[:c+1]
    else:
        a.remove(nums[0])
        a.remove(nums[-1])
        ans=[nums[0]]+a+[nums[-1]]
    print(*ans)