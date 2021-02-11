def sieve(n,choice):
    ans=(n+1)*[True]
    for i in range(2,int(n**0.5)+1):
        if ans[i]:
            for j in range(2*i,n+1,i):
                ans[j]=False
    # ans is the bool array; ans[i] is True if i is prime, false otherwise
    if choice:
        return ans
    res=[]
    for i in range(2,n+1):
        if ans[i]:
            res.append(i)
    # res is the list of primes
    return res
# from time import time
# t1=time()
# ans=(len(sieve(int(input()))))
# t2=time()
# print(ans)
# print('Time:',t2-t1)