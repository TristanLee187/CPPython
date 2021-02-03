rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')


def isPrime(x):
    '''Returns true if x is prime, false otherwise'''
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def primeFactorization2(x):
    '''Returns the prime factorization of x in the form of a 2D array. The first element is the
list of factors, and the second element is the list of exponents. The element with index i in
factors corresponds to the element with index i in exponents.'''
    ps = []
    es = []
    i = 2
    k = x
    while i <= k ** 0.5:
        if k % i == 0 and isPrime(i):
            ps.append(i)
            e = 0
            while k % i == 0:
                k = k // i
                e += 1
            es.append(e)
        i += 1
    if x == 1:
        return [[], []]
    elif isPrime(x):
        return [[x], [1]]
    else:
        return [ps + primeFactorization2(k)[0], es + primeFactorization2(k)[1]]


for _ in range(rn()):
    n=rn()
    prime=primeFactorization2(n)
    if len(prime[0])==1 and prime[1][0]>1:
        print(prime[1][0])
        print(*(prime[1][0]*[prime[0][0]]))
    else:
        ans=max(prime[1])
        print(ans)
        base=prime[0][prime[1].index(ans)]
        pans=ans*[base]
        for i in range(len(prime[0])):
            if prime[0][i]!=base:
                index=-1
                while prime[1][i]>0:
                    pans[index]*=prime[0][i]
                    index-=1
                    prime[1][i]-=1
        print(*pans)