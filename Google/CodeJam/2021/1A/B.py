rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
from collections import defaultdict

for _ in range(rn()):
    ans = 0
    m=rn()
    s=0
    d=defaultdict(int)
    nums=[]
    for i in range(m):
        a=rl()
        s+=a[1]*a[0]
        d[a[0]]=a[1]
        nums.append(a[0])

    def dfs(index,prod,su):
        if prod==s-su:
            global ans
            ans=max(ans,prod)
        if index>=len(nums):
            return
        if prod>s:
            return -1
        num = nums[index]
        for j in range(d[num]+1):
            if dfs(index+1,prod*(1 if j==0 else num**j),su+num*j)==-1:
                return


    dfs(0,1,0)
    print('Case #' + str(_+1)+': ' + str(ans))