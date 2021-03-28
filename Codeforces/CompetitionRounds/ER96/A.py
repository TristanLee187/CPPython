rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

sieve=1001*[-1]
sieve[0]=[0,0,0]
s=[3,5,7]
for i in range(1001):
    if sieve[i]!=-1:
        for j in s:
            if i+j<=1000:
                sieve[i+j]=(sieve[i]).copy()
                sieve[i+j][s.index(j)]+=1

for _ in range(rn()):
    n=rn()
    if sieve[n]==-1:
        print(-1)
    else:
        pl(sieve[n])
