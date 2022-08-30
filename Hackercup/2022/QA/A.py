prob = "second_hands_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

#
# Read input
ans = ''
for t in range(rn()):
    n,k=rns()
    s=rl()
    a=set()
    b=set()
    s.sort()
    pans=True
    for num in s:
        if num not in a and len(a)<k:
            a.add(num)
        elif num not in b and len(b)<k:
            b.add(num)
        else:
            pans=False
            break
    ans+='Case #{}: {}'.format(t+1, 'YES' if pans else 'NO')
    ans+='\n'
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
