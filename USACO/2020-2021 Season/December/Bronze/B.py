n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(n):
    for j in range(i,n):
        s=sum(l[i:j+1])
        if s/(j-i+1) in l[i:j+1]:
            ans+=1
print(ans)