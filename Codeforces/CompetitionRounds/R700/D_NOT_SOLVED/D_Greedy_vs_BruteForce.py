rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
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

n=rn()
def f(n):
    ans=[]
    from random import randrange
    for i in range(n):
        ans.append(randrange(1,4))
    return ans
ans=0
pans=0
while ans==pans:
    l=f(n).copy()
    a = [l[0]]
    b = []
    ans = 1
    for i in range(1, n):
        if l[i] != l[i - 1]:
            ans += 1
            a.append(l[i])
        else:
            b.append(l[i])
    if len(b) > 0:
        ans += 1
    for i in range(1, len(b)):
        if b[i] != b[i - 1]:
            ans += 1

    pans = 0
    wmask = ''
    for i in range(2 ** n):
        tans = 0
        mask = bin(i)[2:]
        while len(mask) < n:
            mask = '0' + mask
        c = []
        e = []
        for i in range(n):
            if mask[i] == '0':
                c.append(l[i])
            else:
                e.append(l[i])
        if len(c) > 0:
            tans += 1
        for j in range(1, len(c)):
            if c[j] != c[j - 1]:
                tans += 1
        if len(e) > 0:
            tans += 1
        for j in range(1, len(e)):
            if e[j] != e[j - 1]:
                tans += 1
        if tans > pans:
            wmask = mask
        pans = max(pans, tans)


print(*l)
print(*a)
print(*b)
print('Greedy:',ans)
print(wmask)
print('Brute Force:',pans)
