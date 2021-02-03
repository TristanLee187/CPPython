t = int(input())
for _ in range(t):
    ans = 2
    n=int(input())
    l=list(map(int,input().split()))

    diffs=[]
    for i in range(1,n):
        diffs.append(l[i]-l[i-1])
    m=2
    for i in range(1,len(diffs)):
        if diffs[i]==diffs[i-1]:
            m+=1
            ans=max(ans,m)
        else:
            m=2
    print('Case #' + str(_ + 1) + ': ' + str(ans))
