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
    s=rs()
    a=[i for i in range(n) if s[i]=='*']
    ans=0
    if len(a) not in [0,1]:
        mid=a[len(a)//2]
        ans=0
        left=0
        right=0
        flag=False
        for i in a:
            ans+=abs(i-mid)
            if i<mid:
                left+=1
            elif i>mid:
                right+=1
            else:
                flag=True
        if not flag:
            ans+=min(left,right)
        ans-=left*(left+1)//2
        ans-=right*(right+1)//2
    print(ans)