for _ in range(int(input())):
    n=int(input())
    d={}
    for i in range(n-1):
        p,c=map(int,input().split())
        if p in d:
            d[p].append(c)
        else:
            d[p]=[c]

