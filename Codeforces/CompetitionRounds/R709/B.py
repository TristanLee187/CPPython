rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    diff=[]
    for i in range(1,n):
        diff.append(a[i]-a[i-1])
    nums=list(set(diff))
    if len(nums)<=1:
        print(0)
    elif len(nums)==2:
        if 0 in nums or nums[0]*nums[1]>0:
            print(-1)
        else:
            poss=abs(nums[0])+abs(nums[1])
            ans=[poss,max(nums)]
            if poss<=max(a):
                print(-1)
            else:
                print(*ans)
    else:
        print(-1)