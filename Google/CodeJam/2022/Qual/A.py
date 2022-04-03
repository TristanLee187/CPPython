from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    ans=[]
    r,c=rns()
    ans += ['..' + ''.join(['+','-'][i%2] for i in range(2*c-1))]
    ans += ['..' + ''.join(['|','.'][i%2] for i in range(2*c-1))]
    ans += [''.join(['+','-'][i%2] for i in range(2*c+1))]
    for i in range(r-1):
        ans += [''.join(['|', '.'][i % 2] for i in range(2 * c + 1))]
        ans += [''.join(['+', '-'][i % 2] for i in range(2 * c + 1))]
    print('Case #' + str(_+1)+':\n' + '\n'.join(ans))