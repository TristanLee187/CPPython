rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

m=998244353
a,b,c=rns()
def f(n):
    return int((((n%m*((n+1)%m))%m)/2)%m)
ans=int(int(f(a)*f(b))%m*(f(c)))%m
print(ans%m)

