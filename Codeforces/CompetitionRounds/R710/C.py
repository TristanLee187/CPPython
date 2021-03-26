rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    a=rs()
    b=rs()
    aset=set()
    aset.add('')
    for i in range(len(a)):
        for j in range(i,len(a)+1):
            aset.add(a[i:j])
    ans=len(a)+len(b)
    for i in range(len(b)):
        for j in range(i,len(b)+1):
            sub=b[i:j]
            if sub in aset:
                ans=min(ans, len(a)+len(b)-2*len(sub))
    print(ans)