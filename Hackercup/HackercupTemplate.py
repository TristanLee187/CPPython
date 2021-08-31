prob = "PROB_NAME"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

#
# Read input
ans = ''
for t in range(rn()):

#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
