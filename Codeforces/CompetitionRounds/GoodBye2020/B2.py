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
    ans=len(set(l))
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for i in d.keys():
        if d[i]>1:
            if i+1 not in d:
                ans+=1
            else:
                d[i+1]+=d[i]-1
    print(ans)