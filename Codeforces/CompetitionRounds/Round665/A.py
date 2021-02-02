t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=max(k-n,0)
    if a==0 and (n-k)%2==1:
        a+=1
    ans=min([abs(n-k),a])
    print(ans)