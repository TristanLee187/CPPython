for _ in range(int(input())):
    x,y,k=map(int,input().split())
    from math import ceil
    a=ceil((k-1)/(x-1))
    total=a*(x-1)+1
    extra=total%k
    b=ceil((k*y-extra)/(x-1))
    ans=a+b+k
    print(int(ans))