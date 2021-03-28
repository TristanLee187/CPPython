for _ in range(int(input())):
    from  math import gcd
    n=int(input())
    l=list(map(int,input().split()))
    m=max(l)
    lm=m
    seen=(m+1)*[0]
    ans=[]
    while len(ans)<n:
        a=[]
        for i in range(n):
            if seen[l[i]]==0 and gcd(lm,l[i])>m:
                a.clear()
                a.append(l[i])
                m=gcd(lm,l[i])
            elif seen[l[i]]==0 and gcd(lm,l[i])==m:
                a.append(l[i])
        ans+=a
        for i in a:
            seen[i]=1
        lm=m
        m=0
    print(' '.join(list(map(str,ans))))