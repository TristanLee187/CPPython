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
pans=0
wmask=''
for i in range(2**n):
    tans=0
    mask=bin(i)[2:]
    while len(mask)<n:
        mask='0'+mask
    c=[]
    e=[]
    for i in range(n):
        if mask[i]=='0':
            c.append(l[i])
        else:
            e.append(l[i])
    if len(c)>0:
        tans+=1
    for j in range(1,len(c)):
        if c[j]!=c[j-1]:
            tans+=1
    if len(e)>0:
        tans+=1
    for j in range(1,len(e)):
        if e[j]!=e[j-1]:
            tans+=1
    if tans>pans:
        wmask=mask
    pans=max(pans,tans)
print(pans)