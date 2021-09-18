from sys import stdin
from itertools import *
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7


def colinear(a, b, c):
    rise1=b[1]-a[1]
    run1=b[0]-a[0]
    rise2=c[1]-b[1]
    run2=c[0]-b[0]
    return rise1*run2 == rise2*run1


def remove_middle(a, b, c):
    cross = (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])
    dot = (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1])
    return not colinear(a,b,c) and (cross < 0 or cross == 0 and dot <= 0)


def convex_hull(points):
    spoints = sorted(points)
    hull = []
    for p in spoints + spoints[::-1]:
        while len(hull) >= 2 and remove_middle(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)
    hull.pop()
    return hull


dist = lambda p1, p2: sum((a - b) * (a - b) for a, b in zip(p1, p2))**0.5

perimeter = lambda *p: sum(dist(i, j) for i, j in zip(p, p[1:] + p[:1]))


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


for _ in range(rn()):
    ans=float('inf')
    n=rn()
    wstars=[tuple(rns()) for __ in range(n)]
    bstar=tuple(rns())
    # print(convex_hull(wstars))

    polys = powerset(wstars)
    for poly in polys:
        if len(poly)>=3:
            if convex_hull(poly) == convex_hull(list(poly)+[bstar]):
                ans=min(ans,perimeter(*convex_hull(poly)))
    if ans==float('inf'):
        ans='IMPOSSIBLE'
    print('Case #' + str(_+1)+': ' + str(ans))