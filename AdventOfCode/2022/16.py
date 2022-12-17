from collections import defaultdict
from heapq import heappop, heappush
from functools import lru_cache


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


file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    v_to_num = defaultdict()
    for i in range(len(lines)):
        tokens = lines[i].split()
        v = tokens[1]
        v_to_num[v] = i
    adj = defaultdict(list)
    rates = defaultdict(int)
    for line in lines:
        tokens = line.split()
        v = tokens[1]
        r = int(tokens[4].split('=')[1][:-1])
        rates[v_to_num[v]] = r
        adj_v = [(v_to_num[a.split(',')[0]], 1) for a in tokens[9:]]
        adj[v_to_num[v]] = adj_v
    ds = []
    for i in range(len(lines)):
        dist = dijkstra(adj, i)[0]
        ds.append(dist)

    # print(v_to_num)
    # print(adj)
    # print(ds)

    def search(node, time, score, visited):
        if time > 30:
            return 0
        ret = score
        for neighbor in rates:
            if rates[neighbor] and (visited & (1 << neighbor) == 0):
                # print(node, neighbor)
                new_time = time + ds[node][neighbor] + 1
                new_score = score + (30 - new_time) * rates[neighbor]
                new_visited = visited | (1 << neighbor)
                ret = max(ret, search(neighbor, new_time, new_score, new_visited))
        return ret

    ans = search(v_to_num['AA'], 0, 0, 1)
    return ans


# part 2
def part_2():
    v_to_num = defaultdict()
    for i in range(len(lines)):
        tokens = lines[i].split()
        v = tokens[1]
        v_to_num[v] = i
    adj = defaultdict(list)
    rates = defaultdict(int)
    non_zeros = []
    for line in lines:
        tokens = line.split()
        v = tokens[1]
        r = int(tokens[4].split('=')[1][:-1])
        rates[v_to_num[v]] = r
        if r:
            non_zeros.append(v_to_num[v])
        adj_v = [(v_to_num[a.split(',')[0]], 1) for a in tokens[9:]]
        adj[v_to_num[v]] = adj_v
    ds = []
    for i in range(len(lines)):
        dist = dijkstra(adj, i)[0]
        ds.append(dist)

    @lru_cache()
    def search(node, enode, time, time2, score, visited):
        if time > 26 or time2 > 26 or bin(visited).count('1')==len(non_zeros):
            return 0
        counter[0] += 1
        if counter[0] % 100000 == 0:
            print(counter[0])
        ret = score
        for i in range(len(non_zeros)):
            for j in range(len(non_zeros)):
                if i == j:
                    continue
                neighbor, neighbor2 = non_zeros[i], non_zeros[j]
                if visited & ((1 << neighbor) | (1 << neighbor2)) == 0:
                    new_time = time + ds[node][neighbor] + 1
                    new_time2 = time2 + ds[enode][neighbor2] + 1
                    new_score = score + (26 - new_time) * rates[neighbor] + (26 - new_time2) * rates[neighbor2]
                    new_visited = visited | (1 << neighbor) | (1 << neighbor2)
                    poss_score = new_score + sum(
                        [(24 - min(new_time, new_time2)) * rates[nnode] for nnode in non_zeros if
                         (new_visited & 1 << nnode == 0)])
                    if poss_score > ret:
                        ret = max(ret, search(neighbor, neighbor2, new_time, new_time2, new_score, new_visited))
                elif (visited & (1 << neighbor) == 0) and (len(non_zeros) - bin(visited).count('1') < 2):
                    new_time = time + ds[node][neighbor] + 1
                    new_score = score + (26 - new_time) * rates[neighbor]
                    new_visited = visited | (1 << neighbor)
                    poss_score = new_score + sum([(24 - new_time) * rates[nnode] for nnode in non_zeros if
                                                  (new_visited & 1 << nnode == 0)])
                    if poss_score > ret:
                        ret = max(ret, search(neighbor, enode, new_time, time2, new_score, new_visited))
        return ret

    counter = [0]
    ans = search(v_to_num['AA'], v_to_num['AA'], 0, 0, 0, 1)
    print(counter[0])
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
