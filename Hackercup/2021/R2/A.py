from collections import Counter

prob = "runway_input"

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
    n,m=rns()
    s=Counter(rl())
    zeros=s.copy()
    ones=Counter()

    rounds=[s]+[Counter(rl()) for _ in range(n)]
    for i in range(n):
        left=Counter()
        for num in rounds[i]:
            if rounds[i][num]>rounds[i+1][num]:
                left[num]=abs(rounds[i][num]-rounds[i+1][num])

        need=Counter()
        for num in rounds[i+1]:
            if rounds[i+1][num]>rounds[i][num]:
                need[num]=rounds[i+1][num]-rounds[i][num]

        take = []
        for num in left:
            take+=[num for _ in range(left[num])]

        for num in need:
            for each in range(need[num]):
                change = take.pop()
                if change in zeros and zeros[change]:
                    zeros[change]-=1
                    ones[num]+=1
                else:
                    pans+=1
                    ones[change]-=1
                    ones[num]+=1

    ans+="Case #{}: {}\n".format(t+1,pans)
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
