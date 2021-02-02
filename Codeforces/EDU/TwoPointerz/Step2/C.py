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
right=0

while left<n and l[left]>s:
    left+=1

if left==n:
    print(0)
else:
    curr=l[left]
    right=left+1
    ans=1
    while left<n and right<n:
        while right<n and curr+l[right]<=s:
            curr+=l[right]
            right+=1
            ans+=1
        curr-=l[left]
        left+=1
        ans+=right-left
    print(ans)