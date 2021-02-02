rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(int(input())):
    n,k,s=rns()
    ans=k-1
    ans+=min(n+1,k-s+n-s+1)
    print('Case #' + str(_ + 1) + ': ' + str(ans))
