from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,c=rns()
    mas=[]
    for i in range(n):
        l,r=rns()
        mas.append((l,1))
        mas.append((r,-1))
    mas.sort()
    vals = [0]
    points = [-float('inf')]
    for i in range(2*n):
        if mas[i][0]==points[-1]:
            vals[-1]+=mas[i][1]
        else:
            points.append(mas[i][0])
            vals.append(vals[-1]+mas[i][1])
    points.append(float('inf'))

    # print(vals)
    # print(points)

    ints=[[] for i in range(len(points))]
    for i in range(len(points)-1,0,-1):
        ints[i]=[vals[i-1],points[i]-points[i-1]-1]
    ints.pop(0)
    for i in range(len(ints)):
        if i<len(ints)-1 and n>1 and ints[i+1][0]>ints[i][0]:
            ints[i][1]+=1
        if i>0 and n>1 and ints[i-1][0]>ints[i][0]:
            ints[i][1]+=1
    ints.sort()

    # print(ints)

    ans=n
    while c>0:
        sub=min(c,ints[-1][1])
        ans+=sub*ints[-1][0]
        if ints[-1][1]==sub:
            ints.pop()
        c-=sub
    ans+=c
    print('Case #' + str(_+1)+': ' + str(ans))
