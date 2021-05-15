from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

s = rs()
ans = [0]


def check(curr, s):
    ans = all([str(i) in curr for i in range(len(s)) if s[i] == 'o'])
    ans = ans and all([str(i) not in curr for i in range(len(s)) if s[i] == 'x'])
    return 1 if ans else 0


def dfs(curr, depth, s, ans):
    if depth == 4:
        ans[-1] += check(curr, s)
        return 0
    for i in range(10):
        dfs(curr + str(i), depth + 1, s, ans)


dfs('', 0, s, ans)
print(ans[0])
