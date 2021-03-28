t = int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))

    ans={}
    for i in range(n):
        for j in range(i,n):
            s=l[i]+l[j]
            if s in ans:
                ans[s]+=1
            else:
                ans[s]=1
    pans=0
    val=0
    for i in ans:
        if ans[i]>=val:
            pans=i
            val=ans[i]
    print(val)