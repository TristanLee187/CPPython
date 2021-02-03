rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
def d(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

for _ in range(rn()):
    from math import ceil
    n,k=rns()
    if n<k:
        print(ceil(k/n))
    elif n==k or k==1:
        print(1)
    else:
        if n%k==0:
            print(1)
        else:
            print(2)