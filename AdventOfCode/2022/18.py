from sys import setrecursionlimit
setrecursionlimit(20**3)

file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    cubes = [tuple(map(int, line.split(','))) for line in lines]
    cubes = list(set(cubes))
    for i in range(len(cubes)):
        total = 6
        ns = set()
        for j in range(len(cubes)):
            if i == j: continue
            found = 0
            n_add = 0
            for k in range(3):
                if cubes[i][k] != cubes[j][k]:
                    found += 1
                if abs(cubes[i][k] - cubes[j][k]) == 1:
                    n_add = cubes[j]
            if found == 1 and type(n_add) != int:
                ns.add(n_add)
        total -= len(ns)
        # print(len(ns), ns)
        ans += total
    return ans


# part 2
def part_2():
    cubes = [tuple(map(int, line.split(','))) for line in lines]
    cubes = list(set(cubes))
    mins = 3 * [float('inf')]
    maxes = 3 * [0]
    for i in range(len(cubes)):
        for j in range(3):
            mins[j] = min(mins[j], cubes[i][j])
            maxes[j] = max(maxes[j], cubes[i][j])
    start = (0, 0, 0)
    deltas = []
    for i in range(3):
        delta = [(0 if i != j else 1) for j in range(3)]
        delta2 = [(0 if i != j else -1) for j in range(3)]
        deltas += [delta, delta2]

    def calc(point, cubes):
        ans = 0
        for d in deltas:
            neigh = tuple([point[i] + d[i] for i in range(3)])
            if neigh in cubes:
                ans += 1
        return ans

    def bfs(point, visited, cubes):
        ans = calc(point, cubes)
        for d in deltas:
            neigh = tuple([point[i] + d[i] for i in range(3)])
            if (neigh not in cubes) and (neigh not in visited) and \
                    all([mins[k]-1 <= neigh[k] <= maxes[k]+1 for k in range(3)]):
                visited.add(neigh)
                ans += bfs(neigh, visited, cubes)
        return ans

    ans = bfs(start, set(), cubes)
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
