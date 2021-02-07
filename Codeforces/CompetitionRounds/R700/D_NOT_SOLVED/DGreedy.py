rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
def d(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

n=rn()
l=rl()
ids=[l[0]]
acc=[0]
for i in range(n):
    if l[i]!=ids[-1]:
        ids.append(l[i])
        acc.append(1)
    else:
        acc[-1]+=1
ans=0
idstack=[]
for i in range(len(ids)):
    if acc[i]==1:
        ans+=1
    else:
        if len(idstack)==0 or idstack[-1]!=ids[-1]:
            ans+=2
            idstack.append(ids[i])
print(ans)