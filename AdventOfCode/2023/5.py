file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()
from pprint import pprint

# part 1
def part_1():
    ans = float('inf')
    seeds = list(map(int, lines[0].split()[1:]))
    maps = []
    curr = []
    for line in lines[2:]:
        if not line:
            maps.append(curr)
            curr = []
        elif 'map' in line:
            pass
        else:
            d, s, r = map(int, line.split())
            curr.append([d,s,r])
    maps.append(curr)
    # pprint(maps)
    for seed in seeds:
        val = seed
        for m in maps:
            for d,s,r in m:
                if s<=val<s+r:
                    val -= s-d
                    break
        # print(seed, val)
        ans=min(ans, val)

    return ans


# part 2
def part_2():
    ans = float('inf')
    seeds = list(map(int, lines[0].split()[1:]))
    maps = []
    curr = []
    for line in lines[2:]:
        if not line:
            curr.sort(key=lambda x: x[1])
            maps.append(curr)
            curr = []
        elif 'map' in line:
            pass
        else:
            d, s, r = map(int, line.split())
            curr.append([d,s,r])
    maps.append(curr)
    # pprint(maps)
    def compute_intersection(a,b,c,d):
        if c<a and d<=a:
            return False
        if b<=c and b<=d:
            return False
        if c<=a<d:
            return (a,min(b,d))
        if c<b<=d:
            return (max(a,c), b)

    for i in range(0, len(seeds), 2):
        val, ran = seeds[i], seeds[i+1]
        print(val, val+ran)
        ranges = {(val, val+ran)}
        # print(ranges)
        for m in maps:
            new_ranges = set()
            for x,y in ranges:
                for i in range(len(m)):
                    d,s,r = m[i]
                    poss1 = compute_intersection(x,y,s,s+r)
                    if poss1:
                        new_ranges.add((poss1[0]-s+d, poss1[1]-s+d))
                    # if s<=x<s+r:
                    #     # x, s+r
                    #     new_ranges.add((x-s+d, r+d))
                    # elif s<y and s+r<=y:
                    #     new_ranges.add((d, r+d))
                        if s>x:
                            if i==0:
                                new_ranges.add((x, s))
                            else:
                                dd,ss,rr = m[i-1]
                                # ss+rr, s
                                poss = compute_intersection(x,y,ss+rr,s)
                                if poss:
                                    new_ranges.add((poss[0]-s+d, poss[1]-s+d))
                        if s+r<y and i==len(m)-1:
                            # ss+rr, y
                            new_ranges.add((s+r, y))
                        

                    # elif s<y<=s+r:
                    #     new_ranges.add((d, y-s+d))
                    #     if i==0:
                    #         new_ranges.add((x, s))
                    #     else:
                    #         dd,ss,rr = m[i-1]
                    #         # ss+rr, s
                    #         poss = compute_intersection(ss,ss+rr,s,s+r)
                    #         if poss:
                    #             new_ranges.add((poss[0]-s+d, poss[1]-s+d))
            if new_ranges:
                ranges = new_ranges
            print(ranges)
        ans = min(ans, min([i[0] for i in ranges]))
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())