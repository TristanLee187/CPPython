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
a=[l[0]]
b=[]
ans=1
for i in range(1,n):
    if l[i]!=l[i-1]:
        ans+=1
        a.append(l[i])
    else:
        b.append(l[i])
if len(b)>0:
    ans+=1
for i in range(1,len(b)):
    if b[i]!=b[i-1]:
        ans+=1
print(ans)