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
    boys={}
    girls={}
    for i in range(k):
        if A[i] not in boys:
            boys[A[i]]=[]
        boys[A[i]].append(B[i])
        if B[i] not in girls:
            girls[B[i]]=0
        girls[B[i]]+=1
    ans=0
    for i in boys:
        for j in boys[i]:
            ans+=k-len(boys[i])-girls[j]+1
    print(ans//2)