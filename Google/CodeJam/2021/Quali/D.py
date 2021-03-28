rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)

t,n,q=rns()
for _ in range(t):
    print(1, 2, 3)
    mid = int(input())
    ans = [1, 2, 3]
    ans.remove(mid)
    ans.insert(1, mid)
    for i in range(4,n+1):
        lo=0
        hi=len(ans)-1
        while lo<hi:
            mid = (lo + hi) // 2
            print(ans[mid],ans[mid+1],i)
            poss=int(input())
            if poss==i:
                ans.insert(mid+1,i)
                break
            elif poss==ans[mid]:
                hi=mid
                if hi<=lo:
                    ans.insert(mid,i)
            else:
                lo=mid+1
                if lo>=hi:
                    ans.insert(mid+2,i)
    print(*ans)
    if rn()==-1:
        break
