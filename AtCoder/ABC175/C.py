x,k,d=map(int,input().split())
x=abs(x)
if x>=k*d:
    print(x-k*d)
else:
    ans=x%d
    a=x//d
    if (k-a)%2==1:
        ans=d-ans
    print(ans)
