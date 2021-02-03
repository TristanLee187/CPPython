rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n,m=rns()
cond=[]
for i in range(m):
    cond.append(rl())
k=rn()
p=[]
for i in range(k):
    p.append(rl())


mask=k*'0'

def check(mask):
    ans=0
    acc=101*[0]
    for i in range(k):
        if mask[i]=='0':
            acc[p[i][0]]+=1
        else:
            acc[p[i][1]]+=1
    for i in cond:
        if acc[i[0]]>0 and acc[i[1]]>0:
            ans+=1
    return ans

ans=check(mask)
for i in range(1,2**k+1):
    mask=bin(i)[2:]
    mask=(k-len(mask))*'0'+mask
    ans=max(ans,check(mask))
print(ans)