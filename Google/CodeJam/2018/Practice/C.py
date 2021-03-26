rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)

for _ in range(rn()):
    ans = 0
    d,n=rns()
    horses=[]
    for i in range(n):
        horses.append(rl())
    horses.sort()
    time = 0
    for i in range(n):
        time = max(time, (d-horses[i][0])/horses[i][1])
    ans = d/time
    print('Case #' + str(_ + 1) + ': ' + str(ans))