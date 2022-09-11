prob = "watering_well_chapter_2_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()
mod=10**9+7

#
# Read input
ans = ''
for t in range(rn()):
    pans=''
    n=rn()
    coors = [rl() for _ in range(n)]
    wells = [rl() for _ in range(rn())]
    # def pre(a):
    #     ans=[a[0]%mod]
    #     for i in range(1, len(a)):
    #         ans.append((ans[-1]+a[i])%mod)
    #     return ans

    def solve(coordinates, well_coordinates, index):
        sum_sq = sum([(coor[index]**2)%mod for coor in coordinates])
        sum_reg = sum([coor[index] for coor in coordinates])
        # print(sum_sq, sum_reg)
        ret = 0
        for coor in well_coordinates:
            ret += sum_sq - 2*sum_reg*coor[index] + n*coor[index]**2
            ret %= mod
            # print(ret)
        return ret
    res = 0
    for i in [0,1]:
        add = solve(coors, wells, i)
        # print(add)
        res += add
        res %= mod
    pans=str(res)
    ans+='Case #{}: {}'.format(t+1, pans)
    ans+='\n'
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
