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
<<<<<<< HEAD
    for num in x:
        pos=0
        for Num in x:
            pos+=min(abs(num-Num),n-abs(num-Num))
=======
    m=max(x)
    for i in range(1,m+1):
        pos=0
        for num in x:
            pos+=min(abs(i-num),n-abs(i-num))
>>>>>>> af72bacd08f89b126d6c7a2536f223afad5a058f
        ans=min(ans,pos)
    print('Case #' + str(_ + 1) + ': ' + str(ans))
