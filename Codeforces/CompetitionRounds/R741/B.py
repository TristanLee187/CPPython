from sys import stdin
from itertools import product
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    k=rn()
    n=rs()
    def f(t):
        s = ''
        for n in t:
            s += n
        s = int(s)
        def isPrime(n):
            if n == 1:
                return False
            for i in range(2, int(n ** 0.5 + 1)):
                if n % i == 0:
                    return False
            return True
        return isPrime(s)

    def check(n,tu):
        p=0
        for i in range(len(n)):
            if n[i]==tu[p]:
                p+=1
            if p==len(tu):
                return True
        return False
    def solve(k,n):
        for num in n:
            if int(num) in [1,4,6,8,9]:
                return [1,int(num)]
        primes=['2','3','5','7']
        i=1
        while i:
            c=product(primes,repeat = i)
            for comb in c:
                if not f(comb) and check(n,comb):
                    return [i,''.join(comb)]
            i+=1
    ans=solve(k,n)
    print(ans[0])
    print(ans[1])
