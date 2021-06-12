from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    p1=[]
    for i in range(n):
        p1.append(rl())
    p2=[]
    for i in range(n):
        p2.append(rl())
    p1.sort()
    p2.sort()
    shift=[p2[0][0]-p1[0][0], p2[0][1]-p1[0][1]]
    for i in range(n):
        p1[i][0]+=shift[0]
        p1[i][1] += shift[1]

