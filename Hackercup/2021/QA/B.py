prob = "xs_and_os_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

#
# Read input
ans = ''
for t in range(rn()):
    n=rn()
    grid=[]
    for _ in range(n):
        grid.append(rs())
    nw=0
    ml=float('inf')
    s=set()
    for row in range(n):
        if 'O' not in grid[row]:
            dots=tuple([(row,i) for i in range(n) if grid[row][i]=='.'])
            need=len(dots)
            if need<ml:
                ml=need
                nw=1
                s=set()
                s.add(dots)
            elif need==ml and dots not in s:
                nw+=1
                s.add(dots)
    for col in range(n):
        column = [grid[i][col] for i in range(n)]
        if 'O' not in column:
            dots = tuple([(i,col) for i in range(n) if column[i] == '.'])
            need = len(dots)
            if need < ml:
                ml = need
                nw = 1
                s = set()
                s.add(dots)
            elif need == ml and dots not in s:
                nw += 1
                s.add(dots)
    if nw==0:
        ans+='Case #{}: Impossible\n'.format(t+1)
    else:
        ans += 'Case #{}: {} {}\n'.format(t + 1,ml,nw)
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
