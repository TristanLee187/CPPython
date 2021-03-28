rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)

for _ in range(rn()):
    ans=0

    n = rn()
    a = rl()
    for i in range(n - 1):
        j = a.index(min(a[i:]))
        ans += j - i + 1
        a = a[:i] + a[i:j + 1][::-1] + a[j + 1:]
    print('Case #' + str(_+1)+': ' + str(ans))