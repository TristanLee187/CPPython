for _ in range(int(input())):
    from  math import gcd
    n=int(input())
    l=list(map(int,input().split()))
    m=max(l)
    ans=[]
    for i in range(n):
        l[i] = [(gcd(m,l[i])),l[i]]
    l.sort(reverse=True)
    print(l)
    ans=[i[1] for i in l]
    print(' '.join(list(map(str,ans))))

