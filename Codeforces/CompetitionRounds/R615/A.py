for _ in range(int(input())):
    a,b,c,n = map(int,input().split())
    l=sorted([a,b,c])
    n-=l[-1]-l[0]+l[-1]-l[1]
    if n>=0 and n%3==0:
        print('YES')
    else:
        print('NO')