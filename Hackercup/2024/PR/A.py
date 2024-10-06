prob = "walk_the_line_input"

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
    n,k=rns()
    s=[rn() for _ in range(n)]
    m=min(s)
    if max(0,2*m*(n-2))+m <= k:
        pans='YES'
    else:
        pans='NO'

    ans+='Case #{}: {}'.format(t+1, pans)
    ans+='\n'
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
