mod = 2 ** 32
n = int(input())
start = [[0]*65 for i in range(65)]
start[0][0]=1
mult = [[0]*65 for i in range(65)]

for row in range(8):
    for col in range(8):
        for dr in [-2,-1,1,2]:
            for dc in [-2,-1,1,2]:
                if abs(dr)!=abs(dc):
                    nrow=row+dr
                    ncol=col+dc
                    if 0<=nrow<=7 and 0<=ncol<=7:
                        mult[8*row+col][8*nrow+ncol] = 1

for row in range(64):
    mult[-1][row]=1


def matrix_mult(a, b):
    n = len(b)
    m = len(a[0])
    ans = [[0] * m for j in range(n)]
    i = 0
    while i < n:
        j = 0
        while j < m:
            k = 0
            while k < n:
                ans[i][j] += a[k][j] * b[i][k]
                if ans[i][j] > mod:
                    ans[i][j] -= mod
                k += 1
            j += 1
        i += 1
    return ans


def eye(m):
    """returns an indentity matrix of order m"""
    identity = [[0] * m for _ in range(m)]
    i = 0
    while i < m:
        identity[i][i] = 1
        i += 1
    return identity


def mat_pow(mat, power):
    """returns mat**power"""

    result = eye(len(mat))
    if power == 0:
        return result

    while power > 1:
        if power & 1:
            result = matrix_mult(result, mat)
        mat = matrix_mult(mat, mat)
        power >>= 1
    return matrix_mult(result, mat)


ans=1
for i in range(n):
    start=matrix_mult(start,mult)
    for row in start:
        ans+=sum(row[:-1])
        ans%=mod
print(ans)
print(sum([start[row][0] for row in range(65)]))
