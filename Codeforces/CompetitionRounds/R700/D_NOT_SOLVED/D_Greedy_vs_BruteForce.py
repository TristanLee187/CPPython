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
    ids = [l[0]]
    acc = [0]
    for i in range(n):
        if l[i] != ids[-1]:
            ids.append(l[i])
            acc.append(1)
        else:
            acc[-1] += 1
    ans = 0
    idstack = []
    for i in range(len(ids)):
        if acc[i] == 1:
            ans += 1
        else:
            if len(idstack) == 0 or idstack[-1] != ids[-1]:
                ans += 2
                idstack.append(ids[i])

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
print(*ids)
print(*acc)
print('Greedy:',ans)
print(wmask)
print('Brute Force:',pans)
