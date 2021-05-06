from sys import stdin, stdout
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,t=rns()
k=rn()

lo=1
hi=n
while lo<hi:
    mid=(lo+hi)//2
    print('?',1,mid)
    stdout.flush()
    left=rn()
    if mid-left==k:
        hi=mid
    elif mid-left<k:
        lo=mid+1
    else:
        hi=mid-1
print('!',lo)