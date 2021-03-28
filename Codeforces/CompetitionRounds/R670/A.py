for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    freq=101*[0]
    for i in l:
        freq[i]+=1
    ans=0
    c=0
    for i in range(101):
        if freq[i]<2:
            ans+=i
            break
    add=0
    import bisect
    for i in range(102):
        j=bisect.bisect_left(l,i)
        if j==len(l) or l[bisect.bisect_left(l,i)]!=i:
            add=i
            break
    print(ans+add)