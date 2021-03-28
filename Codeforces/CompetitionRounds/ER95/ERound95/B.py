for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=list(map(int,input().split()))

    s=[l[i] for i in range(n) if a[i]==0]
    s.sort(reverse=True)
    j=0
    for i in range(n):
        if a[i]==0:
            l[i]=s[j]
            j+=1
    print(' '.join(list(map(str,l))))
