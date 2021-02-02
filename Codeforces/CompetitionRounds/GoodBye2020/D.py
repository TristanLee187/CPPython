rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n=rn()
    l=rl()
    d=(n+1)*[0]
    for i in range(n-1):
        u,v=rns()
        d[u]+=1
        d[v]+=1
    sums=[]
    for i in range(1,n+1):
        sums+=[l[i-1]]*(d[i]-1)
    sums.sort(reverse=True)
    ans=[sum(l)]
    for i in sums:
        ans.append(ans[-1]+i)
    print(*ans)
