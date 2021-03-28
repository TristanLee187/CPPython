def isPrime(x):
    if x==1:
        return False
    else:
        ans=True
        for i in range(2, int(x**0.5)+1):
            if x%i==0:
                ans=False
                break
        return ans

def diffPrime(x, l):
    if x==1:
        return -1
    else:
        ans = -1
        comp = l[0]
        for i in range(len(l)):
            if x%l[i]==0 and l[i]<=comp:
                comp=l[i]
                ans = i
        return ans


n=int(input())
k=n

ans=0

primes = []
for i in range(2, int(n**0.5)+1):
    if isPrime(i):
        primes.append(i)

primes2 = list(primes)

index = diffPrime(n, primes2)
while index!=-1:
    ans+=1
    n = n//primes2[index]
    primes2[index] *= primes[index]
    index = diffPrime(n, primes2)
    print(primes2)
    

if k==1:
    print(0)
elif isPrime(k):
    print(1)
else:
    print(ans)

            
            
            
    

