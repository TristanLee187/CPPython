mod = 2 ** 32
n = int(input()) + 1
start = [[0] * 65 for _ in range(65)]
start[0][0] = 1
mult = [[0] * 65 for _ in range(65)]
for row in range(8):
    for col in range(8):
        for dr in [-2, -1, 1, 2]:
            for dc in [-2, -1, 1, 2]:
                if abs(dr) != abs(dc):
                    nrow = row + dr
                    ncol = col + dc
                    if 0 <= nrow <= 7 and 0 <= ncol <= 7:
                        mult[8 * row + col][8 * nrow + ncol] = 1
for row in range(65):
    mult[-1][row] = 1


def matrix_mult(a, b):
    ans = [[0] * 65 for j in range(65)]
    i = 0
    while i < 65:
        j = 0
        while j < 65:
            k = 0
            while k < 65:
                ans[i][j] += (a[k][j] * b[i][k]) % mod
                ans[i][j] %= mod
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
    if not power:
        return result

    while power - 1:
        if power & 1:
            result = matrix_mult(result, mat)
        mat = matrix_mult(mat, mat)
        power >>= 1
    return matrix_mult(result, mat)


print(matrix_mult(start, mat_pow(mult, n))[-1][0])
