from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    h,w=rns()
    ans=[w*['0'] for i in range(h)]
    ans[0] = ['1' if i%2==0 else '0' for i in range(w)]
    for i in range(2,h):
        ans[i][-1]='1' if i and i%2==0 else '0'
    for i in range(w-2):
        ans[-1][i]='1' if i%2==0 else '0'
    for i in range(2,h-2):
        ans[i][0]='1' if i%2==0 else '0'
    for row in ans:
        print(''.join(row))
