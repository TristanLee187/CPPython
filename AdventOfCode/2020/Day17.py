a='''.#.
..#
###'''.split('\n')

grid=[]
for count in range(15):
    cube=[]
    if count==7:
        for i in range(15):
            if i==7:
                plane = []
                for j in range(len(a) + 14):
                    if 7<=j<len(a)+7:
                        plane.append(7*['.']+list(a[j-7])+7*['.'])
                    else:
                        plane.append((len(a) + 14) * ['.'])
                cube.append(plane)
            else:
                plane=[]
                for j in range(len(a)+14):
                    plane.append((len(a)+14)*['.'])
                cube.append(plane)
    else:
        for i in range(15):
            plane=[]
            for j in range(len(a)+14):
                plane.append((len(a)+14)*['.'])
            cube.append(plane)
    grid.append(cube)

row=1
index=6
for count in range(6):
    new=[]
    for i in grid:
        new.append([])
        for j in i:
            new[-1].append([])
            for k in j:
                new[-1][-1].append([])
                for l in k:
                    new[-1][-1][-1].append(l)
    for c in range(7-row,7+row+1):
        for i in range(7-row,7+row+1):
            for j in range(index,len(grid[0])-index):
                for k in range(index,len(grid[0])-index):
                    ps=[]
                    for s in range(c-1,c+2):
                        for m in range(i-1,i+2):
                            for n in range(j-1,j+2):
                                for o in range(k-1,k+2):
                                    if s!=c or m!=i or n!=j or o!=k:
                                        try:
                                            ps.append(grid[s][m][n][o])
                                        except:
                                            print(s,m,n,o)
                    if grid[i][j][k]=='#':
                        if ps.count('#') in [2,3]:
                            new[i][j][k]='#'
                        else:
                            new[i][j][k]='.'
                    else:
                        if ps.count('#')==3:
                            new[i][j][k]='#'
                        else:
                            new[i][j][k]='.'
    row+=1
    index-=1
    grid=new.copy()

ans=0
for i in grid:
    for j in i:
        for k in j:
            ans+=k.count('#')
print(grid[7][7])
print(ans)