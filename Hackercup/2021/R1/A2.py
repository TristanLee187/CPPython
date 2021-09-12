prob = "weak_typing_chapter_2_input"
from collections import Counter
file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()
mod = 10**9+7

#
# Read input
ans = ''
for t in range(rn()):
    n=rn()
    w=rs()
    pre=[0]
    last=float('inf')
    if 'O' in w:
        last=w.index('O')
    if 'X' in w:
        last=min(last,w.index('X'))
    if last==float('inf'):
        last=0
    last=w[last]

    for char in w:
        if char not in ['F',last]:
            last=char
            pre.append(pre[-1]+1)
        else:
            pre.append(pre[-1])
    pre.pop(0)
    w=reversed(w)
    changes=[0]
    for char in w:
        if char not in ['F',last]:
            last=char
            changes.append(1)
        else:
            changes.append(0)
    changes.reverse()
    changes.pop()
    pans = 0
    add = sum(pre)%mod
    c = len([i for i in pre if i != 0])
    counter=Counter(pre)
    counts=[i[1] for i in sorted(counter.items(),reverse=True)[:-1]]
    for i in range(n):
        pans+=add
        pans%=mod
        if changes[i]:
            add-=c
            c-=counts.pop()
    ans+="Case #{}: {}\n".format(t+1, pans)
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
