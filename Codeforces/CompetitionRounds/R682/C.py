rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
pl = lambda l: print(' '.join(list(map(str, l))))
for _ in range(rn()):
    n,m=rns()
    mat=[]
    for i in range(n):
        mat.append(rl())
    for i in range(n):
        for j in range(m):
            if i%2==j%2:
                mat[i][j]+=mat[i][j]%2
            else:
                mat[i][j] += int(not(mat[i][j] % 2))
    for i in mat:
        print(*i)