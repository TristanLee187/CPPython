s=int(input())
ans=0
m=0
while s-m*3>=3:
    t=s-m*3
    if t==3:
        ans+=1
    else:
        ans+=m+1
    ans%=10**9+7
    m+=1
print(ans)