rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')

for _ in range(rn()):
    n,k=rns()
    l=rl()
    curr=1
    for i in range(1,k-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            curr+=1
    ans=curr
    le=1
    for i in range(1,n-k+1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            curr-=1
        if i+k-2<n-1 and l[i+k-2]>l[i+k-3] and l[i+k-2]>l[i+k-1]:
            curr+=1
        if curr>ans:
            ans=curr
            le=i+1
    print(ans,le)
        
    
