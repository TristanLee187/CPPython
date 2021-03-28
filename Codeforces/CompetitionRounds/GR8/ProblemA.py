

t=int(input())
count=0
while count<t:
    count+=1
    a,b,n = map(int, input().split(' '))
    A=max(a,b)
    B=min(a,b)
    nums=[0,1]
    ans=0
    while nums[-1]*A+nums[-2]*B<=n:
        ans+=1
        nums.append(nums[-1]+nums[-2])
    print(ans)
    
    
