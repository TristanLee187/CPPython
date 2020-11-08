rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

s=rs()
digs={i:0 for i in range(10)}
for i in s:
    digs[int(i)]+=1

ans=False
l=[i for i in range(8,1001,8) if len(str(i))==len(s) or (len(s)>=3 and len(str(i))==3)]
for i in l:
    d={j:0 for j in range(10)}
    for c in str(i):
        d[int(c)]+=1
    cd=[j for j in d if d[j]>0]
    if all([digs[j]>=d[j] for j in cd]):
        ans=True
        break

yn(ans)

