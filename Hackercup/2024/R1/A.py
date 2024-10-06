prob = "subsonic_subway_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()


def div(a,b):
    if b==0:
        return float('inf')
    return a/b
#
# Read input
ans = ''
for t in range(rn()):
    pans=''
    n=rn()
    stations=[]
    for _ in range(n):
        a,b=rns()
        stations.append((a,b))
    mms = []
    for i in range(n):
        pair = (div(i+1, stations[i][1]), div(i+1, stations[i][0]))
        mms.append(pair)
    box=[mms[0][0], mms[0][1]]
    for pair in mms[1:]:
        if pair[0] > box[0]:
            box[0] = pair[0]
        if pair[1] < box[1]:
            box[1] = pair[1]
    if box[0] > box[1]:
        pans = -1
    else:
        pans = box[0]
    ans+='Case #{}: {}'.format(t+1, pans)
    ans+='\n'
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
