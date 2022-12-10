file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    c = 1
    x = 1
    l = []
    for line in lines:
        if line == 'noop':
            l+=['noop']
        else:
            l+=['noop',int(line.split()[1])]
    for line in l:
        if c in [20,60,100,140,180,220]:
            ans+=c*x
            print(c*x)
        c+=1
        if type(line)==int:
            x+=line
    return ans


# part 2
def part_2():
    ans = []
    c = 0
    x = 1
    l = []
    for line in lines:
        if line == 'noop':
            l+=['noop']
        else:
            l+=['noop',int(line.split()[1])]
    for line in l:
        pos=c%40
        if pos in [x-1,x,x+1]:
            ans.append('#')
        else:
            ans.append('.')
        if type(line)==int:
            x+=line
        c+=1
    for i in range(6):
        print(''.join(ans[40*i:40*(i+1)]))


if __name__ == '__main__':
    print(part_1())
    part_2()
