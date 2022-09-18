from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

def ceildiv(a, b):
    return -(a // -b)

for _ in range(rn()):
    ans=0
    d,n,x=rns()
    seeds=[rl() for i in range(n)]
    seeds.sort(key=lambda x: (-x[1], -x[2]))
    curr_x = x
    i=0
    while i<n:
        q,l,v=seeds[i]
        if d <= l:
            i+=1
        elif curr_x==x:
            times=d-l
            needed_days = q//x
            actual_days = min(times, needed_days)
            actual_seeds = min(actual_days*x, q)
            ans += actual_seeds*v
            d -= actual_days
            if d>l:
                curr_x -= q%x
                ans += (q%x) * v
            i+=1
        else:
            actual_seeds = min(curr_x, q)
            ans+=actual_seeds*v
            curr_x-=actual_seeds
            seeds[i][0]-=actual_seeds
            if curr_x==0:
                curr_x=x
                d-=1


    print('Case #' + str(_+1)+': ' + str(ans))