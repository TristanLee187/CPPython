for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    p=list(map(int,input().split()))
    l=sorted(a)
    index=[]
    for i in range(n):
        if a[i]!=l[i]:
            index.append(i)