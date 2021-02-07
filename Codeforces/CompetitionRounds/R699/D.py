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

for _ in range(rn()):
    n,m=rns()
    grid=[]
    for i in range(n):
        grid.append(rs())
    if m%2==1:
        print('YES')
        print((m+1)//2*'1 2 ')
    else:
        flag=False
        pair=''
        for i in range(n):
            for j in range(n):
                if i!=j and grid[i][j]==grid[j][i]:
                    flag=True
                    pair=str(i+1)+' '+str(j+1)+' '
                    break
        if flag:
            print('YES')
            print(m//2*pair+pair.split()[0])
        else:
            if n==2:
                print('NO')
            else:
                triplet=[]
                for i in range(n):
                    if len(set(grid[i]))==3:
                        triplet=[i+1,grid[i].index('a')+1,grid[i].index('b')+1]
                        break
                a=str(triplet[0])+' '+str(triplet[1])+' '
                b=str(triplet[2])+' '+str(triplet[0])+' '
                print('YES')
                if (m//2)%2==0:
                    print(m//4*a + str(triplet[0])+' '+m//4*b)
                else:
                    m-=2
                    print(str(triplet[1])+' '+m // 4 * a + str(triplet[0]) + ' ' + m // 4 * b+str(triplet[2]))