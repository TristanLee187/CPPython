rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)

for _ in range(rn()):
    n,c=rns()
    ans=''
    if c<n-1 or c>n*(n+1)//2-1:
        ans='IMPOSSIBLE'
    else:
        def solve(cost, length, num):
            if length-1>=cost:
                ret = list(range(num,num+cost+1))[::-1] + list(range(num+cost+1,num+length))
                return ret
            return solve(cost-(length-1),length-1,num+1)[::-1] + [num]

        ans = solve(c-n+1,n,1)
        ans=' '.join(list(map(str,ans)))
    print('Case #' + str(_+1)+': ' + str(ans))