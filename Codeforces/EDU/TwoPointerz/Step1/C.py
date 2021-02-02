rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n,m=rns()
a=rl()
b=rl()
A={}
for i in a:
    if i in A:
        A[i]+=1
    else:
        A[i]=1
B={}
for i in b:
    if i in B:
        B[i]+=1
    else:
        B[i]=1
ans=0
for i in A:
    if i in B:
        ans+=B[i]*A[i]
print(ans)
