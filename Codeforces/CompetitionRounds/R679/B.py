rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n,m=rns()
    rows=[]
    for i in range(n):
        rows.append(rl())
    cols=[]
    for i in range(m):
        cols.append(rl())
    c=0
    for i in range(m):
        if rows[0][0] in cols[i]:
            c=i
            break
    d=501*[0]
    for i in range(n):
        d[cols[c][i]]=i
    rows.sort(key=lambda x: d[x[0]])
    for i in rows:
        print(*i)

