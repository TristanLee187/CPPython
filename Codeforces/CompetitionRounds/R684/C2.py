rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n, m = rns()
    l = []
    for i in range(n):
        l.append(rs())
    nans=0
    ans=[]
    for i in range(0,n-n%2,2):
        for j in range(0,m-m%2,2):
            a=[l[i][j], l[i+1][j+1], l[i][j+1], l[i+1][j]]
            if a.count('1')==1:
                nans+=3
                k=a.index('1')
                if k==0:
                    ans.append([i+1,j+1,i+1,j+2,i+2,j+1])
                    ans.append([i+1,j+1,i+1,j+2,i+2,j+2])
                    ans.append([i+1,j+1,i+2,j+2,i+2,j+1])
                elif k==1:
                    ans.append([i + 1, j + 1, i + 1, j, i, j + 1])
                    ans.append([i + 1, j + 1, i , j, i , j + 1])
                    ans.append([i + 1, j + 1, i , j , i +1, j])
                elif k==2:
                    ans.append([i + 1, j + 1, i + 1, j , i + 2, j + 1])
                    ans.append([i + 1, j + 1, i + 2, j , i + 2, j + 1])
                    ans.append([i + 1, j + 1, i + 2, j, i + 1, j ])
                else:
                    ans.append([i + 1, j + 1, i + 1, j + 2, i , j + 1])
                    ans.append([i + 1, j + 1, i , j + 2, i + 1, j + 2])
                    ans.append([i + 1, j + 1, i , j + 2, i , j + 1])
            elif a.count('0')==1:
                ans+=1
                k=a.index('0')
                if k==0:
                    ans.append([i + 2, j + 2, i + 1, j + 2, i + 2, j + 1])
                elif k==1:
                    ans.append([i + 1, j , i , j + 1, i , j ])
                elif k==2:
                    ans.append([i + 1, j , i + 1, j + 2, i + 2, j ])
                else:
                    ans.append([i + 1, j + 2, i , j + 1, i , j + 2])

            elif a[0]==a[1]=='1':
                
            elif a[2]==a[3]=='1':