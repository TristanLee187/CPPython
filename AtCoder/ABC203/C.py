from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

n,k=rns()
f=[]
for i in range(n):
    f.append(rl())
f.sort()
ans=0
for i in range(n+1):
    if i==n or f[i][0]>ans+k:
        ans+=k
        break
    else:
        ans=f[i][0]
        if i==0:
            k-=f[i][0]
        else:
            k-=f[i][0]-f[i-1][0]
        k+=f[i][1]
print(ans)
