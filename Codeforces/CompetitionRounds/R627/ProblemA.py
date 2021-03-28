t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int, input().split(' ')))
    ans=True
    for i in range(n-1):
        if (l[i]-l[i+1])%2!=0:
            ans=False
            break
    if ans:
        print("YES")
    else:
        print("NO")
        
