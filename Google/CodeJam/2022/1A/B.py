from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7


def naive(nums, target):
    ans=[]
    if target%1==0:
        rem = target%10
    else:
        rem = 4.5
    ans.append(rem)
    target-=rem
    mod=-1
    if target%10!=0:
        mod=target%10
        target-=mod
        ans.append(mod)
    for num in nums:
        if target==0:
            return ans
        if num not in [rem, 10-rem, mod, 10-mod] and not (num==1 and len(nums)==8):
            ans += [num, 10-num]
            target-=10

for _ in range(rn()):
    n=rn()
    a=[]
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    nums2 = [1, 2, 3, 4, 4.5, 5, 5.5, 6, 7, 8, 9]
    snums = sum(nums)
    snums2=sum(nums2)

    for i in range(9):
        c = nums.copy() if i==0 else nums2.copy()
        for num in c:
            a.append(int(num*10**i))
    a += [10**9 - i for i in range(4)]
    print(*a)

    b=rl()
    b.sort()
    set1=set()
    set2=set()
    for i in range(n//2):
        if i%2==0:
            set1.add(b[i])
            set1.add(b[n-i-1])
        else:
            set2.add(b[i])
            set2.add(b[n-i-1])
    diff=sum(set1) - sum(set2)
    if diff<0:
        set1, set2 = set2.copy(), set1.copy()
    set1.add(10**9)
    set1.add(10**9-3)
    for i in range(9):
        dig = diff%10
        diff //= 10
        add=set()
        if i==0:
            add = naive(nums, snums/2-dig/2)
        else:
            add = naive(nums2, snums2/2-dig/2)
        for num in add:
            set1.add(int(num*10**i))
    ans = ' '.join(map(str,set1))
    print('Case #' + str(_+1)+': ' + ans)
