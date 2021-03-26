rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)

for _ in range(rn()):
    d,p=input().split()
    d=int(d)
    p=list(p)

    if d<p.count('S'):
        print('IMPOSSIBLE')
    else:
        ans = 0
        def f(a):
            ret=0
            add=1
            for i in a:
                if i=='S':
                    ret+=add
                else:
                    add*=2
            return ret
        comp=f(p)
        while comp>d:
            for i in range(len(p)-2,-1,-1):
                if p[i]=='C' and p[i+1]=='S':
                    p[i],p[i+1] = p[i+1],p[i]
                    ans+=1
                    comp=f(p)
                    break
        print('Case #' + str(_ + 1) + ': ' + str(ans))