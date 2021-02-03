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

n=rn()
a=rl()
b=rl()
m1=a[0]
m2=b[0]
ans=m1*m2
print(ans)
for i in range(1,n):
    if a[i]>m1:
        m1=a[i]
        ans=max(a[i]*b[i],ans)
    elif b[i]*m1>ans:
        m2=b[i]
        ans=m1*m2
    print(ans)
