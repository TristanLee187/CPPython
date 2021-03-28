t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    r-=r%2
    if r<2*l:
        print(-1,-1)
    else:
        print(r//2,r)
        
