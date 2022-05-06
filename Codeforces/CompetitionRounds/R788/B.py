from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n=rn()
    s=rs()
    spec=rs().split()
    num_spec=int(spec[0])
    specs = spec[1:]
    indeces = [i for i in range(n) if s[i] in specs]
    diff=[indeces[i+1]-indeces[i] for i in range(len(indeces)-1)]
    if len(indeces)>0:
        diff=[indeces[0]] + diff
    if len(diff)>0:
        print(max(diff))
    else:
        print(0)