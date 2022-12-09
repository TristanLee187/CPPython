file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    seen=set()
    seen.add((0,0))
    a,b=0,0
    c,d=0,0
    for line in lines:
        direction,step = line.split()
        step=int(step)
        for i in range(step):
            if direction=='U':
                b+=1
            elif direction=='D':
                b-=1
            elif direction=='L':
                a-=1
            else:
                a+=1
            xdiff=a-c
            ydiff=b-d
            if (xdiff==-2 and ydiff>0) or (xdiff==-1 and ydiff==2):
                c-=1
                d+=1
            elif (xdiff==0 and ydiff==2):
                d+=1
            elif (xdiff==2 and ydiff>0) or (xdiff==1 and ydiff==2):
                c+=1
                d+=1
            elif (xdiff==2 and ydiff==0):
                c+=1
            elif (xdiff==2 and ydiff<0) or (xdiff==1 and ydiff==-2):
                c+=1
                d-=1
            elif (xdiff==0 and ydiff==-2):
                d-=1
            elif (xdiff==-2 and ydiff<0) or (xdiff==-1 and ydiff==-2):
                c-=1
                d-=1
            elif (xdiff==-2 and ydiff==0):
                c-=1
            seen.add((c,d))
    return len(seen)


# part 2
def part_2():
    ans = 0
    seen=set()
    seen.add((0,0))
    points=[[0,0] for i in range(10)]
    for line in lines:
        direction,step = line.split()
        step=int(step)
        for i in range(step):
            if direction=='U':
                points[0][1]+=1
            elif direction=='D':
                points[0][1]-=1
            elif direction=='L':
                points[0][0]-=1
            else:
                points[0][0]+=1
            for p in range(1,10):
                xdiff = points[p-1][0] - points[p][0]
                ydiff = points[p-1][1] - points[p][1]
                if (xdiff == -2 and ydiff > 0) or (xdiff == -1 and ydiff == 2):
                    points[p][0] -= 1
                    points[p][1] += 1
                elif (xdiff == 0 and ydiff == 2):
                    points[p][1] += 1
                elif (xdiff == 2 and ydiff > 0) or (xdiff == 1 and ydiff == 2):
                    points[p][0] += 1
                    points[p][1] += 1
                elif (xdiff == 2 and ydiff == 0):
                    points[p][0] += 1
                elif (xdiff == 2 and ydiff < 0) or (xdiff == 1 and ydiff == -2):
                    points[p][0] += 1
                    points[p][1] -= 1
                elif (xdiff == 0 and ydiff == -2):
                    points[p][1] -= 1
                elif (xdiff == -2 and ydiff < 0) or (xdiff == -1 and ydiff == -2):
                    points[p][0] -= 1
                    points[p][1] -= 1
                elif (xdiff == -2 and ydiff == 0):
                    points[p][0] -= 1
            seen.add((points[-1][0], points[-1][1]))
    return len(seen)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
