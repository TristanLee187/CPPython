rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)
from math import gcd

for _ in range(rn()):
    n,l=rns()
    a=rl()
    nums=(l+1)*[0]
    for i in range(l-1):
        if a[i]!=a[i+1]:
            g = gcd(a[i],a[i+1])
            nums[i+1]=g
            for j in range(i,-1,-1):
                nums[j] = a[j]//nums[j+1]
            for j in range(i+1,l):
                nums[j+1] = a[j]//nums[j]
            break

    keys=sorted(list(set(nums)))
    d={keys[i]: chr(i+65) for i in range(len(keys))}

    ans = ''
    for num in nums:
        ans+=d[num]

    print('Case #' + str(_ + 1) + ': ' + ans)