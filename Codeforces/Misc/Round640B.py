for _ in range(int(input())):
    n,k=map(int,input().split())
    if (n-(k-1))%2==1 and (n-k+1)>0:
        print('YES')
        print((k-1)*'1 '+str(n-k+1))
    elif ((n-(k-1)*2)%2==0 and (n-(k-1)*2)>0):
        print('YES')
        print((k-1)*'2 '+str(n-2*k+2))
    else:
        print('NO')
        
