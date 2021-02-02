rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')

for _ in range(rn()):
    from math import ceil

    n, m = rns()
    l = []
    for i in range(n):
        l.append(rl())
    ans = 0
    c=0
    for i in range(n):
        for j in range(m):
            points = []
            points.append(l[i][j])
            points.append(l[i][m - j - 1])
            points.append(l[n - i - 1][j])
            points.append(l[n - 1 - i][m - j - 1])
            points.sort()
            ans += points[1]-points[0]
            ans+=points[2]-points[1]
            ans+=points[3]-points[1]
    print(ans//4)