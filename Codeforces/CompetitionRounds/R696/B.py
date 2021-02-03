rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

sieve=20012*[0]
primes=[]
for i in range(2,len(sieve)):
    if sieve[i]==0:
        primes.append(i)
        for j in range(i,len(sieve),i):
            sieve[j]=1

for _ in range(rn()):
    d=rn()
    from bisect import bisect_left
    a=primes[bisect_left(primes,1+d)]
    b=primes[bisect_left(primes,a+d)]
    print(a*b)