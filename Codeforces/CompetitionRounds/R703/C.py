rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
def d(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=0
        d[i]+=1
    return d

n=rn()
lo=1
hi=n
print('? ' + str(lo) + ' ' + str(hi))
j = rn()
while lo<hi-1:
    mid=(lo+hi+1)//2
    if j <= mid:
        print('? ' + str(lo) + ' ' + str(mid))
        k=rn()
        if k == j:
            j=k
            hi = mid
        else:
            lo = mid
            print('? ' + str(lo) + ' ' + str(hi))
            j = rn()
    else:
        print('? ' + str(mid) + ' ' + str(hi))
        k = rn()
        if k == j:
            j=k
            lo = mid
        else:
            hi = mid
            print('? ' + str(lo) + ' ' + str(hi))
            j = rn()

ans=0
if j==lo:
    ans=hi
else:
    ans=lo

print('! '+str(ans))