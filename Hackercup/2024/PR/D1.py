prob = "line_of_delivery_part_1_input"

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
    n,g=rns()
    e=[rn() for _ in range(n)]
    e.sort()
    curr_best = float('inf')
    for i in range(n):
        if abs(e[i]-g) <= curr_best:
            pans=i
            curr_best=abs(e[i]-g)
    pans = f'{n-pans} {curr_best}'
    ans+='Case #{}: {}'.format(t+1, pans)
    ans+='\n'
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
