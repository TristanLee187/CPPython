from collections import Counter
file = open("input.txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

a = int(rs()[-1])
b = int(rs()[-1])
file.close()
req = 21
ascore = 0
bscore = 0
rolls = []
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            rolls.append(i + j + k)
c = Counter(rolls)


# print(c)
def dfs(u, index, asc, bsc, apos, bpos):
    if asc >= req:
        return [u, 0]
    if bsc >= req:
        return [0, u]
    ans = [0, 0]
    if index % 2 == 0:
        for roll in c:
            napos = (apos + roll) % 10
            if napos == 0:
                napos = 10
            nasc = asc + napos
            res = dfs(u * c[roll], index + 1, nasc, bsc, napos, bpos)
            ans[0] += res[0]
            ans[1] += res[1]
    else:
        for roll in c:
            nbpos = (bpos + roll) % 10
            if nbpos == 0:
                nbpos = 10
            nbsc = bsc + nbpos
            res = dfs(u * c[roll], index + 1, asc, nbsc, apos, nbpos)
            ans[0] += res[0]
            ans[1] += res[1]
    return ans


print(max(dfs(1, 0, 0, 0, a, b)))
