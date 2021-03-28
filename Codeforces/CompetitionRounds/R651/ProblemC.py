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


def solve(n):
    if n==1:
        return False
    else:
        l=primeFactorization2(n)
        things = 0
        for i in range(len(l[0])):
            if l[0][i]%2==1:
                things += l[1][i]
        if things==0:
            return n>2
        else:
            something=l[1][0]
            if something==1:
                return things<2
            else:
                return False

def dummy(x):
    l=primeFactorization2(x)
    things = 0
    for i in range(len(l[0])):
        if l[0][i]%2==1:
            things += l[1][i]
    return things
    
        
        
    
t=int(input())
count=0
while count<t:
    count+=1
    n=int(input())
    if n==1:
        print("FastestFinger")
    elif n%2==1:
        print("Ashishgup")
    else:
        if solve(n):
            print("FastestFinger")
        else:
            print("Ashishgup")
            
        
        
        
        
            
        
    
    
    
    
