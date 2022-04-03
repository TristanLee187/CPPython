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
    p=[rl() for i in range(3)]
    ans = []
    for i in range(4):
        nums = [p[j][i] for j in range(3)]
        ans.append(min(nums))
    if sum(ans)<10**6:
        ans = 'IMPOSSIBLE'
    else:
        c = 0
        while 10**6 != sum(ans):
            diff = sum(ans)-10**6
            if ans[c]>diff:
                ans[c]-=diff
                break
            ans[c]=1
            c+=1
        ans = ' '.join(list(map(str,ans)))

    print('Case #' + str(_+1)+': ' + str(ans))

