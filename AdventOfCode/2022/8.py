file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    grid=[[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    # from left
    for i in range(len(lines)):
        m=lines[i][0]
        grid[i][0]=1
        for j in range(1,len(lines[0])):
            if lines[i][j]>m:
                m=lines[i][j]
                grid[i][j]=1
    # from right
    for i in range(len(lines)):
        m=lines[i][len(lines[0])-1]
        grid[i][len(lines[0])-1]=1
        for j in range(len(lines[0])-1,-1,-1):
            if lines[i][j]>m:
                m=lines[i][j]
                grid[i][j]=1
    # from top
    for i in range(len(lines[0])):
        m=lines[0][i]
        grid[0][i]=1
        for j in range(len(lines)):
            if lines[j][i]>m:
                m=lines[j][i]
                grid[j][i]=1
    # from bottom
    for i in range(len(lines[0])):
        m=lines[-1][i]
        grid[-1][i]=1
        for j in range(len(lines)-1,-1,-1):
            if lines[j][i]>m:
                m=lines[j][i]
                grid[j][i]=1
    ans = sum([sum(line) for line in grid])
    return ans


# part 2
def part_2():
    ans = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            a=[0]
            n=lines[i][j]
            # look left
            for k in range(j-1,-1,-1):
                a[-1]+=1
                if lines[i][k]>=n:
                    break
            a.append(0)
            # look right
            for k in range(j+1,len(lines[0])):
                a[-1]+=1
                if lines[i][k]>=n:
                    break
            a.append(0)
            # look up
            for k in range(i-1,-1,-1):
                a[-1]+=1
                if lines[k][j]>=n:
                    break
            a.append(0)
            # look down
            for k in range(i+1,len(lines)):
                a[-1]+=1
                if lines[k][j]>=n:
                    break
            ans=max(ans,a[0]*a[1]*a[2]*a[3])

    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
