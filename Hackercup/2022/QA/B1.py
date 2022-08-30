prob = "second_friend_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

#
# Read input
ans = ''
for t in range(rn()):
    pans = ''
    r,c=rns()
    grid=[list(rs()) for i in range(r)]
    trees=False
    for row in grid:
        if '^' in row:
            trees=True
            break

    if not trees:
        pans='Possible\n'
        for i in range(r):
            pans+=c*'.' + '\n'
    elif 1 in [r,c]:
        pans='Impossible\n'
    else:
        pans='Possible\n'
        for i in range(r):
            pans+=c*'^' + '\n'

    ans += 'Case #{}: {}'.format(t + 1, pans)
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
