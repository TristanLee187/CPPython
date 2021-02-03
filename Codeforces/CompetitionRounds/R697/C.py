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
    a,b,k=rns()
    A=rl()
    B=rl()
    d={}
    for i in range(k):
        if A[i] in d:
            d[A[i]].add(B[i])
        else:
            d[A[i]]=set()
            d[A[i]].add(B[i])
    c={}
    # pairs=[[A[i],B[i]] for i in range(k)]
    # pairs.sort()
