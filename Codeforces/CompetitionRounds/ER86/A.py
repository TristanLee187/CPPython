for _ in range(int(input())):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if b<2*a:
        ans=b*min(x,y)
        ans+=a*(max(x,y)-min(x,y))
        print(ans)
    else:
        ans=(x+y)*a
        print(ans)