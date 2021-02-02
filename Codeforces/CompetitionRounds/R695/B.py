rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
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

for _ in range(rn()):
    n=rn()
    l=rl()
    a=n*[0]
    for i in range(1,n-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            a[i]=1
        elif l[i]>l[i-1] and l[i]>l[i+1]:
            a[i]=-1
    ans=sum(list(map(abs,a)))
    m=0
    for i in range(1,n-1):
        if abs(a[i])==1 and a[i-1]==a[i+1]==0:
            m=max(m,1)
