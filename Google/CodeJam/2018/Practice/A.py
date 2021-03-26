rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)

for _ in range(rn()):
    a,b=rns()
    lo=a+1
    hi=b
    n=rn()
    while True:
        mid=(lo+hi)//2
        print(mid)
        ver = rs()
        if ver=='CORRECT':
            break
        elif ver=='TOO_SMALL':
            lo=mid+1
        else:
            hi=mid-1