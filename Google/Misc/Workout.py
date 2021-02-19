from math import ceil
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    diff=[l[i]-l[i-1] for i in range(1,n)]
    lo=1
    hi=max(diff)
    ans=hi
    while lo<=hi:
        mid=(lo+hi+1)//2
        acc=0
        for i in diff:
            acc+=ceil(i/mid)-1
        if acc<=k:
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    print('Case #' + str(_+1)+': ' + str(ans))