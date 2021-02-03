a=[]
for i in range(91):
    a.append([i for i in input()])
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]=='L':
            a[i][j]='#'
def get(i,j,a):
    c = []
    for k in range(j+1,len(a[0])):
        if a[i][k]!='.':
            c.append(a[i][k])
            break
    for k in range(1,len(a[0])):
        if i-k<0 or j+k>=len(a[0]):
            break
        if a[i-k][j+k]!='.':
            c.append(a[i-k][j+k])
            break
    for k in range(i-1,-1,-1):
        if a[k][j]!='.':
            c.append(a[k][j])
            break
    for k in range(1,len(a[0])):
        if i-k<0 or j-k<0:
            break
        if a[i-k][j-k]!='.':
            c.append(a[i-k][j-k])
            break
    for k in range(1,len(a[0])):
        if i+k>=len(a) or j-k<0:
            break
        if a[i+k][j-k]!='.':
            c.append(a[i+k][j-k])
            break
    for k in range(1,len(a[0])):
        if i+k>=len(a) or j+k>=len(a[0]):
            break
        if a[i+k][j+k]!='.':
            c.append(a[i+k][j+k])
            break
    for k in range(j-1,-1,-1):
        if a[i][k]!='.':
            c.append(a[i][k])
            break
    for k in range(i+1,len(a)):
        if a[k][j]!='.':
            c.append(a[k][j])
            break
    return c.count('#')
change=1
while change!=0:
    b = []
    for i in range(len(a)):
        b.append([])
        for j in range(len(a[0])):
            b[-1].append('')
    change=0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]=='L':
                if get(i,j,a)==0:
                    b[i][j]='#'
                    change+=1
                else:
                    b[i][j]=a[i][j]
            elif a[i][j]=='#':
                if get(i,j,a)>=5:
                    b[i][j]='L'
                    change+=1
                else:
                    b[i][j]=a[i][j]
            else:
                b[i][j]=a[i][j]
    a=b.copy()
ans=0
for i in a:
    for j in i:
        if j=='#':
            ans+=1

print(ans)
