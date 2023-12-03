from collections import defaultdict

file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    for i in range(len(lines)):
        curr=''
        leftbound=-1
        for j in range(len(lines[0])):
            if lines[i][j].isnumeric():
                curr+=lines[i][j]
                if leftbound==-1:
                    leftbound=j
                if j==len(lines[0])-1:
                    rightbound = j
                    for k in range(i-1, i+2):
                        flag=False
                        for l in range(leftbound-1, rightbound+2):
                            if 0<=k<len(lines) and 0<=l<len(lines[0]) and not(lines[k][l].isnumeric()) and lines[k][l]!='.':
                                ans+=int(curr)
                                flag=True
                                break
                        if flag:
                            break
                    curr=''
                    leftbound=-1
            elif len(curr):
                rightbound = j-1
                for k in range(i-1, i+2):
                    flag=False
                    for l in range(leftbound-1, rightbound+2):
                        if 0<=k<len(lines) and 0<=l<len(lines[0]) and not(lines[k][l].isnumeric()) and lines[k][l]!='.':
                            ans+=int(curr)
                            flag=True
                            break
                    if flag:
                        break
                curr=''
                leftbound=-1
    return ans


# part 2
def part_2():
    ans = 0
    gears=defaultdict(list)
    for i in range(len(lines)):
        curr=''
        leftbound=-1
        for j in range(len(lines[0])):
            if lines[i][j].isnumeric():
                curr+=lines[i][j]
                if leftbound==-1:
                    leftbound=j
                if j==len(lines[0])-1:
                    rightbound = j
                    for k in range(i-1, i+2):
                        for l in range(leftbound-1, rightbound+2):
                            if 0<=k<len(lines) and 0<=l<len(lines[0]) and lines[k][l]=='*':
                                gears[(k,l)].append(int(curr))
                    curr=''
                    leftbound=-1
            elif len(curr):
                rightbound = j-1
                for k in range(i-1, i+2):
                    for l in range(leftbound-1, rightbound+2):
                        if 0<=k<len(lines) and 0<=l<len(lines[0]) and lines[k][l]=='*':
                            gears[(k,l)].append(int(curr))
                curr=''
                leftbound=-1
    for gear in gears:
        if len(gears[gear])==2:
            ans += gears[gear][0] * gears[gear][1]
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())