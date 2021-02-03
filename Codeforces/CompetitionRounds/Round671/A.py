for _ in range(int(input())):
    n=int(input())
    x=list(map(int,list(input())))
    a=0
    b=0
    for i in range(n):
        if i%2==0:
            a+=(x[i]%2==1)
        else:
            b+=(x[i]%2==0)
    if n%2==1:
        if a>0:
            print(1)
        else:
            print(2)
    else:
        if b>0:
            print(2)
        else:
            print(1)


