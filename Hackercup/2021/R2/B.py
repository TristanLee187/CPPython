from collections import defaultdict
import sys
sys.setrecursionlimit(800000)

prob = "chainblock_validation_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

#
# Read input
ans = ''
for t in range(rn()):
    road_set=set()
    roads=defaultdict(list)
    n=rn()
    for _ in range(n-1):
        a,b=rns()
        roads[a].append(b)
        roads[b].append(a)
        road_set.add((a,b))
    paths={}
    def dfs(root,paths,roads,path):
        newpath=path+[root]
        paths[root]=newpath
        for child in roads[root]:
            if child != root:
                dfs(child,paths,roads,newpath)
    dfs(1,paths,roads,[1])
    a=rl()
    freqs=defaultdict(list)
    for i in range(n):
        freqs[a[i]].append(i+1)
    pans = 0
    # print(paths)
    for freq in freqs:
        npaths = [paths[num][::-1] for num in freqs[freq]]
        # print(freq,npaths)
        m=float('inf')
        for i in npaths:
            m=min(m,len(i))
        while m>=2 and all([npaths[i][-2] == npaths[0][-2] for i in range(len(npaths))]):
            for i in range(len(npaths)):
                npaths[i].pop()
            m-=1

        for path in npaths:
            for i in range(len(path)-1):
                a,b=path[i],path[i+1]
                if (a,b) in road_set:
                    road_set.remove((a,b))
                if (b,a) in road_set:
                    road_set.remove((b,a))
    pans=len(road_set)
    ans += "Case #{}: {}\n".format(t + 1, pans)
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
