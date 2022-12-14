file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    grid=[['.' for i in range(200)] for j in range(440,520)]
    start_x= 440
    for line in lines:
        path=line.split('->')
        prev_x=-1
        prev_y=-1
        for pair in path:
            x,y=map(int,pair.split(','))
            if prev_x==-1:
                prev_x=x
                prev_y=y
                grid[x-start_x][y]='#'
            elif prev_x==x:
                for i in range(min(prev_y,y), max(prev_y,y)+1):
                    grid[x-start_x][i] = '#'
                prev_x=x
                prev_y=y
            else:
                for i in range(min(prev_x,x), max(prev_x,x)+1):
                    grid[i-start_x][y] = '#'
                prev_x = x
                prev_y = y

    grid[500 - start_x][0] = '+'
    while True:
        ans+=1
        x,y = 500,0
        while True:
            if grid[x-start_x][y+1] != '.':
                if grid[x-start_x-1][y+1] == '.':
                    x-=1
                    y+=1
                elif grid[x-start_x+1][y+1] == '.':
                    x+=1
                    y+=1
                else:
                    grid[x - start_x][y] = 'O'
                    break
            else:
                y+=1
            if y > 180:
                return ans


# part 2
def part_2():
    ans = 0
    grid=[['.' for i in range(200)] for j in range(1000)]
    start_x= 0
    maxy=0
    for line in lines:
        path=line.split('->')
        prev_x=-1
        prev_y=-1
        for pair in path:
            x,y=map(int,pair.split(','))
            maxy=max(maxy,y)
            if prev_x==-1:
                prev_x=x
                prev_y=y
                grid[x-start_x][y]='#'
            elif prev_x==x:
                for i in range(min(prev_y,y), max(prev_y,y)+1):
                    grid[x-start_x][i] = '#'
                prev_x=x
                prev_y=y
            else:
                for i in range(min(prev_x,x), max(prev_x,x)+1):
                    grid[i-start_x][y] = '#'
                prev_x = x
                prev_y = y
    for i in range(1000):
        grid[i][maxy+2] = '#'
    grid[500 - start_x][0] = '+'
    while True:
        ans+=1
        x,y = 500,0
        while True:
            if grid[x-start_x][y+1] != '.':
                if grid[x-start_x-1][y+1] == '.':
                    x-=1
                    y+=1
                elif grid[x-start_x+1][y+1] == '.':
                    x+=1
                    y+=1
                else:
                    grid[x - start_x][y] = 'O'
                    if x==500 and y==0:
                        return ans
                    break
            else:
                y+=1


if __name__ == '__main__':
    print(part_1())
    print(part_2())
