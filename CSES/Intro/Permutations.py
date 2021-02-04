n=int(input())
if n==2 or n==3:
    print('NO SOLUTION')
else:
    o=[i for i in range(1,n+1) if i%2==1]
    e=[i for i in range(1,n+1) if i%2==0]
    ans=e+o
    print(*ans)