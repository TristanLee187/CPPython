from math import ceil
file=open("input.txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

alg=rs()
rs()
n=100
grid=[list(rs()) for i in range(n)]
truegrid=[['.' for i in range(500)] for j in range(int(ceil((500-n)/2)))]
for i in range(n):
    truegrid.append(['.' for j in range((500-n)//2)]+grid[i]+['.' for j in range(int(ceil((500-n)/2)))])
truegrid+=[['.' for i in range(500)] for j in range(int(ceil((500-n)//2)))]
file.close()
def strtonum(string):
    ans=0
    for i in range(len(string)):
        if string[i]=='#':
            ans+=2**(len(string)-i-1)
    return ans
for step in range(50):
    newgrid=[['.' for i in range(500)] for j in range(500)]
    for i in range(1,499):
        for j in range(1,499):
            string = ''
            for k in range(-1,2):
                for l in range(-1,2):
                    string+=truegrid[i+k][j+l]
            b=strtonum(string)
            newgrid[i][j]=alg[b]
    if step%2==0:
        for i in range(500):
            newgrid[0][i]=alg[0]
        for i in range(500):
            newgrid[499][i]=alg[0]
        for i in range(500):
            newgrid[i][0]=alg[0]
        for i in range(500):
            newgrid[i][499]=alg[0]
    else:
        for i in range(500):
            newgrid[0][i] = alg[-1]
        for i in range(500):
            newgrid[499][i] = alg[-1]
        for i in range(500):
            newgrid[i][0] = alg[-1]
        for i in range(500):
            newgrid[i][499] = alg[-1]
    truegrid=newgrid
ans=0
rows=[]
# for i in range(500):
#     if '#' in truegrid[i]:
#         rows.append(i)
for row in truegrid:
    for i in row:
        if i=='#':
            ans+=1
print(ans)
# print(truegrid[1])
