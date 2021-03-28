for _ in range(int(input())):
    n=int(input())
    def isPrime(x):
        '''Returns true if x is prime, false otherwise'''
        if x == 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    def primeFactorization2(x):
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
    l=primeFactorization2(n)
    flag=True
    ans=[]
