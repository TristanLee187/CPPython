rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
def d(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

n=rn()
low=1
high=n
while low!=high:
    mid=(low+high+1)//2
    reads=[]
    if mid==1:
        print('? '+str(mid))
        reads.append(rn())
        print('? '+str(mid+1))
        reads.append(rn())
    elif mid==n:
        print('? '+str(mid-1))
        reads.append(rn())
        print('? ' + str(mid))
        reads.append(rn())
    else:
        print('? ' + str(mid - 1))
        reads.append(rn())
        print('? ' + str(mid))
        reads.append(rn())
        print('? ' + str(mid + 1))
        reads.append(rn())
    if reads==sorted(reads):
        high=mid-1
    else:
        low=mid
print('! '+str(low))