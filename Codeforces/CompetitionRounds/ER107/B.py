from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

primes=[2,3,11,13,101,103,1009,1013,10007,10009,100003,100019,1000003,1000033,10000019,10000079,100000007,100000037]

for _ in range(rn()):
    a,b,c=rns()
    mul=10**(c-1)
    ans=[0,0]
    for i in primes:
        if len(str(i))==a-c+1:
            ans[0]=(i*mul)
            a=-1
        elif len(str(i))==b-c+1:
            ans[1]=(i*mul)
            b=-1
    print(*ans)