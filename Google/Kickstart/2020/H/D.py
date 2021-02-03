rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))
from bisect import bisect

for _ in range(int(input())):
    ans = []
    n,q=rns()
    l=input().split()
    calls=[]
    for i in range(q):
        calls.append(rl())
    a=[]
    for i in range(n):
        a.append([])
        b=[]
        for j in range(n):
            for c in l[i]:
                if c in l[j]:
                    b.append(j)
                    break
        a[-1].append(b)
    net=a.copy()
    for i in range(n):
        a[i]=a[i][0]
    for i in range(n):
        b=[]
        for j in net[i][-1]:
            b+=a[j]
        b=list(set(b))
        while b!=net[i][-1]:
            net[i].append(b.copy())
            for j in net[i][-1]:
                b += a[j]
            b = list(set(b))

    for i in range(q):
        call=calls[i]
        pans=-1
        for j in range(len(net[call[0]-1])):

            if call[1]-1 in net[call[0]-1][j]:
                pans=j+2
                break
        ans.append(pans)

    print('Case #' + str(_ + 1) + ': ' + ' '.join(list(map(str,ans))))
