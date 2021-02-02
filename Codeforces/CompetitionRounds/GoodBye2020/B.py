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

    for i in range(1,n-1):
        if l[i]==l[i-1] and l[i+1]>l[i] and (d[l[i+1]]==1):
            ans+=1
    if n>1 and l[-1]==l[-2]:
        ans+=1
    print(ans)