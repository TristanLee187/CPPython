t=int(input())
for z in range(t):
    n,r = map(int, input().split(' '))
    if r==1:
        print(1)
    elif n>r:
        ans=r*(r+1)//2
        print(ans)
    else:
        ans=n*(n-1)//2+1
        print(ans)
        
        
    
