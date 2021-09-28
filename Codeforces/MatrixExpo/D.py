from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
mod = 10 ** 9 + 7


def matrix_mult(a, b):
    n = len(b)
    m = len(a[0])
    ans = [[0] * m for j in range(n)]
    i=0
    while i<n:
        j = 0
        while j<m:
            k = 0
            while k<n:
                ans[i][j] += a[k][j] * b[i][k]
                ans[i][j]%=mod
                k+=1
            j+=1
        i+=1
    return ans


def eye(m):
    """returns an indentity matrix of order m"""
    identity = [[0] * m for _ in range(m)]
    i=0
    while i<m:
        identity[i][i]=1
        i+=1
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


n, m, k = rns()
mat = [[0] * n for j in range(n)]
for _ in range(m):
    a, b = rns()
    mat[a - 1][b - 1] = 1
mat_ans = mat_pow(mat, k)
ans = 0
for i in mat_ans:
    ans += sum(i)
    ans%=mod

print(ans)
