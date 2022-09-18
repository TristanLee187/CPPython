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
    ans=0
    n=rn()
    def clean(x):
        return [x[0], int(x[1]), int(x[2])]
    f=[clean(rs().split()) for _ in range(n)]
    a = sorted(f, key=lambda x: (x[0], x[2]))
    b = sorted(f, key=lambda x: (x[1], x[2]))
    # print(a)
    # print(b)

    for i in range(n):
        if a[i][2]==b[i][2]:
            ans+=1
    print('Case #' + str(_+1)+': ' + str(ans))