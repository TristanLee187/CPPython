prob = "cottontail_climb_part_1_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

#
# Read input
ans = ''
for t in range(rn()):
    pans=0
    a,b,m = rns()
    for k in range(0, 9):
        for dig in range(1,10):
            num = ''.join([str(j) for j in range(dig, dig+k)]) + str(dig+k) + \
                ''.join([str(j) for j in range(dig+k-1,dig-1,-1)])
            # print(num)
            if len(num) == 2*k+1 and (a<=int(num)<=b) and int(num)%m==0:
                pans+=1
    ans+='Case #{}: {}'.format(t+1, pans)
    ans+='\n'
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
