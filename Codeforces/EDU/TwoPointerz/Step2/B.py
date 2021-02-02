rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n,s=rns()
l=rl()
left=0
curr=l[0]
right=1
while right<n and curr<s:
    curr+=l[right]
    right+=1
if curr<s:
    print(-1)
else:
    ans=right-left
    while left<n and right<=n:
        while left<n and curr>=s:
            curr-=l[left]
            left+=1
        tans=right-left
        if curr<s:
            tans+=1
        ans=min(ans,tans)
        if right==n:
            break
        curr+=l[right]
        right+=1
    print(ans)