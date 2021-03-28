for _ in range(int(input())):
    n,x,y=map(int,input().split())
    d=y-x
    factor=1
    for i in range(2,n):
        if d%i==0:
            factor=i
    diff=d//factor
    factor-=1
    n-=factor+2
    pre=x-min(n,(x-1)//diff)*diff
    n-=min(n,(x-1)//diff)
    suff=y+n*diff
    l=[]
    for i in range(pre,suff+1,diff):
        l.append(i)
    print(' '.join(list(map(str,l))))