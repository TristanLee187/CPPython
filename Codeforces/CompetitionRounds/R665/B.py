t = int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    ans=min(c,y)*2
    c-=min(c,y)
    y-=min(c,y)

    z-=min(z,c+a)
    ans-=2*z
    print(ans)


