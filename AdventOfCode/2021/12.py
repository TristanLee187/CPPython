from collections import defaultdict

prob="input"

file=open(prob+".txt")

rn=lambda:int(line)
rns=lambda:map(int,line.split())
rl=lambda:list(map(int,line.split()))
rs=lambda:line.strip()

ans=0
lines=file.readlines()
n=len(lines)
graph=defaultdict(list)
for line in lines:
    a,b=rs().split('-')
    graph[a].append(b)
    graph[b].append(a)
# for node in graph:
#     print(node, graph[node])
# print(graph)
def dfs(graph, curr, seen, arr, flag):
    # print('wtf', curr)
    for child in graph[curr]:
        if child!='start':
            if child == 'end':
                arr[0]+=1
                # print(seen)
            else:
                if child.islower():
                    if child not in seen:
                        new_seen=seen.copy()
                        new_seen.add(child)
                        dfs(graph, child, new_seen, arr, flag)
                    elif flag:
                        pass
                    else:
                        dfs(graph, child, seen, arr, True)
                else:
                    dfs(graph, child, seen, arr, flag)

file.close()
arr=[0]
dfs(graph, 'start', set(), arr, False)
print(arr[0])
