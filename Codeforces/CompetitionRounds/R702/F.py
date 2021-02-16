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

for _ in range(rn()):
    n=rn()
    l=rl()
    dic=d(l)
    dic2=d(list(dic.values()))
    ans=n
    for i in dic2:
        acc=0
        for j in dic2:
            if i!=j:
                if j<i:
                    acc+=j*dic2[j]
                else:
                    acc+=(j-i)*dic2[j]
        ans=min(ans,acc)
    print(ans)
