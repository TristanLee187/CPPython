n=int(input())
if n<=7:
    print("codeforces" + (n-1)*"s")
else:
    def isPrime(x):
        if x==1:
            return False
        for i in range(2, int(x**0.5)+1):
            if x%i==0:
                return False
        return True

    def primeFactorization2(x):
        ps = []
        es = []
        i=2
        k=x
        while i<=k**0.5:
            if k%i==0 and isPrime(i):
                ps.append(i)
                e=0
                while k%i==0:
                    k = k//i
                    e+=1
                es.append(e)
            i+=1
        if x==1:
            return [[],[]]
        elif isPrime(x):
            return [[x],[1]]
        else:
            return [ps + primeFactorization2(k)[0], es + primeFactorization2(k)[1]]

    while isPrime(n):
        n+=1

    l=primeFactorization2(n)

    ans=""
    string="codeforces"   

    factors = l[0]
    exps = l[1]

    
    while len(factors)<10:
        factors.append(1)
        exps.append(1)

    tfactors = 10*[1]

    def minIndex(l):
        ans=0
        for i in range(len(l)):
            if l[i]<l[ans]:
                ans=i
        return ans
    
    i=len(factors)-1
    while i>=0:
        j=exps[i]
        while j>0:
            j-=1
            tfactors[minIndex(tfactors)]*=factors[i]
        i-=1
    for i in range(10):
        ans += tfactors[i]*string[i]
    print(ans)
    print(tfactors)
        

    
    
    
