rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n,k=rns()
    l=rl()
    ans=0
    from math import ceil
    i=n*k-1-(n-ceil(n/2))
    c=0
    while c<k:
        ans+=l[i]
        i-=(n-ceil(n/2)+1)
        c+=1



    print(ans)