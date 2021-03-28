t=int(input())
for _ in range(t):
    n=int(input())
    if n<31:
        print('NO')
    else:
        n-=6+10+14
        if n==6 or n==10 or n==14:
            print('YES')
            print(' '.join(['6','10','15',str(n-1)]))
        else:
            print('YES')
            print(' '.join(['6','10','14',str(n)]))