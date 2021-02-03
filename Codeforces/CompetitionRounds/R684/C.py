rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n,m=rns()
    l=[]
    for i in range(n):
        l.append(rs())
    ans=0
    for i in l:
        ans+=i.count('1')
    ans*=3
    print(ans)
    for i in range(n):
        for j in range(m):
            if l[i][j]=='1':
                a=[i+1,j+1]
                if i==n-1:
                    a.append(i)
                else:
                    a.append(i+2)
                if j==m-1:
                    a.append(j)
                else:
                    a.append(j+2)
                a+=[a[0],a[3],a[2],a[1]]
                print(*[a[0],a[1],a[2],a[3],a[4],a[5]])
                print(*[a[0], a[1], a[2], a[3], a[6], a[7]])
                print(*[a[0], a[1], a[4], a[5], a[6], a[7]])

