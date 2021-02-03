rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(int(input())):
    ans = 0
    l,r=rns()
    def good(n):
        for i in range(len(str(n))):
            if int(not(i%2))!=int(str(n)[i])%2:
                return False
        return True
    for i in range(l,r+1):
        if good(i):
            ans+=1
    print('Case #' + str(_ + 1) + ': ' + str(ans))
