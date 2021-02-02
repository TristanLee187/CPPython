n=int(input())
ans=0
for i in range(1,n):
    r=(n-1)//i
    ans+=r
print(ans)