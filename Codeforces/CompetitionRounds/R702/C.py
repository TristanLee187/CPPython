rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
def d(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=0
        d[i]+=1
    return d

sieve=[]
for i in range(1,10**4+1):
    sieve.append(i**3)
for _ in range(rn()):
    x=rn()
    ans=False
    i=0
    j=10**4-1
    while j<len(sieve) and i>=0 and sieve[i]+sieve[j]!=x and j>=i:
        if sieve[i] + sieve[j] == x:
            ans=True
            break
        elif sieve[i]+sieve[j]<x:
            i+=1
        else:
            j-=1
    if sieve[i] + sieve[j] == x:
        ans = True
    YN(ans)