prob = "second_second_friend_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

#
# Read input
ans = ''
for t in range(rn()):
    pans=''
    r, c = rns()
    grid = [list(rs()) for i in range(r)]
    trees = False
    for row in grid:
        if '^' in row:
            trees = True
            break

    if not trees:
        pans = 'Possible\n'
        for row in grid:
            pans += ''.join(row) + '\n'
    elif 1 in [r, c]:
        pans = 'Impossible\n'
    else:
        flag=True
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='.':
                    neighbors=0
                    if j>0 and grid[i][j-1] != '#':
                        neighbors+=1
                    if j<c-1 and grid[i][j+1] != '#':
                        neighbors+=1
                    if i>0 and grid[i-1][j] != '#':
                        neighbors+=1
                    if i<r-1 and grid[i+1][j] != '#':
                        neighbors+=1
                    if neighbors>=2:
                        grid[i][j]='^'

        for i in range(r):
            for j in range(c):
                if grid[i][j]=='^':
                    neighbors=0
                    if j>0 and grid[i][j-1] == '^':
                        neighbors+=1
                    if j<c-1 and grid[i][j+1] == '^':
                        neighbors+=1
                    if i>0 and grid[i-1][j] == '^':
                        neighbors+=1
                    if i<r-1 and grid[i+1][j] == '^':
                        neighbors+=1
                    if neighbors<2:
                        flag=False
                        break

        if flag:
            pans = 'Possible\n'
            for row in grid:
                pans+=''.join(row) + '\n'
        else:
            pans='Impossible\n'
    ans+='Case #{}: {}'.format(t+1, pans)
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
