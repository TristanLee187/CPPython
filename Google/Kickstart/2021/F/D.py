from sys import stdin
from collections import defaultdict
from itertools import *
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


for _ in range(rn()):
    ans=0
    n,m,k=rns()
    rooms=[tuple(rns()) for __ in range(n)]
    paths=defaultdict(list)
    for __ in range(m):
        x,y=rns()
        paths[x].append(y)
        paths[y].append(x)

    for subset in powerset(range(n)):
        pp = sum([rooms[room][2] for room in subset])
        if pp==k:
            for path in permutations(subset):
                flag = True
                seen={path[0]}
                magic=rooms[path[0]][2]
                for nextroom in path[1:]:
                    poss = any([nextroom in paths[room] for room in seen])
                    if poss and rooms[nextroom][0]<=magic<=rooms[nextroom][1]:
                        seen.add(nextroom)
                        magic+=rooms[nextroom][2]
                    else:
                        flag=False
                        break
                ans+=flag

    print('Case #' + str(_+1)+': ' + str(ans))