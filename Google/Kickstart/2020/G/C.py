rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(int(input())):
    ans = float('inf')
    w,n=rns()
    x=rl()
    for num in x:
        pos=0
        for Num in x:
            pos+=min(abs(num-Num),n-abs(num-Num))
        ans=min(ans,pos)
    print('Case #' + str(_ + 1) + ': ' + str(ans))
