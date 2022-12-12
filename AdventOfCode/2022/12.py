file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()

from heapq import heappop, heappush


def dijkstra(graph, start):
    """
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents


def f(coors):
    return coors[0] * len(lines[0]) + coors[1]


# part 1
def part_1():
    ans = 0
    start = []
    end = []
    grid = [[]]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'S':
                start += [i, j]
                grid[-1].append(ord('a'))
            elif lines[i][j] == 'E':
                end += [i, j]
                grid[-1].append(ord('z'))
            else:
                grid[-1].append(ord(lines[i][j]))
        grid.append([])
    g = dict()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            neighbors = []
            if i > 0 and grid[i - 1][j] < grid[i][j] + 2:
                neighbors.append((i - 1, j))
            if i < len(lines) - 1 and grid[i + 1][j] < grid[i][j] + 2:
                neighbors.append((i + 1, j))
            if j > 0 and grid[i][j - 1] < grid[i][j] + 2:
                neighbors.append((i, j - 1))
            if j < len(lines[0]) - 1 and grid[i][j + 1] < grid[i][j] + 2:
                neighbors.append((i, j + 1))
            g[f((i, j))] = []
            for n in neighbors:
                g[f((i, j))].append((f(n), 1))
    d, p = dijkstra(g, f(start))
    ans = d[f(end)]
    return ans


# part 2
def part_2():
    ans = float('inf')
    start = []
    end = []
    grid = [[]]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] in ['S', 'a']:
                start.append([i, j])
                grid[-1].append(ord('a'))
            elif lines[i][j] == 'E':
                end += [i, j]
                grid[-1].append(ord('z'))
            else:
                grid[-1].append(ord(lines[i][j]))
        grid.append([])
    g = dict()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            neighbors = []
            if i > 0 and grid[i][j] < grid[i - 1][j] + 2:
                neighbors.append((i - 1, j))
            if i < len(lines) - 1 and grid[i][j] < grid[i + 1][j] + 2:
                neighbors.append((i + 1, j))
            if j > 0 and grid[i][j] < grid[i][j - 1] + 2:
                neighbors.append((i, j - 1))
            if j < len(lines[0]) - 1 and grid[i][j] < grid[i][j + 1] + 2:
                neighbors.append((i, j + 1))
            g[f((i, j))] = []
            for n in neighbors:
                g[f((i, j))].append((f(n), 1))
    d, p = dijkstra(g, f(end))
    for s in start:
        ans = min(ans, d[f(s)])
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
