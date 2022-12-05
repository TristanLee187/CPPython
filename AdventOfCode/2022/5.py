file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = ''
    d={
        1:list('STHFWR'),
        2:list('SGDQW'),
        3:list('BTW'),
        4:list('DRWTNQZJ'),
        5:list('FBHGLVTZ'),
        6:list('LPTCVBSG'),
        7:list('ZBRTWGP'),
        8:list('NGMTCJR'),
        9:list('LGBW')
    }
    for i in range(10,512):
        line=lines[i].split()
        a,b,c=int(line[1]),int(line[3]),int(line[5])
        for j in range(a):
            d[c].append(d[b].pop())
    for i in range(1,10):
        ans+=d[i][-1]
    return ans


# part 2
def part_2():
    ans = ''
    d={
        1:list('STHFWR'),
        2:list('SGDQW'),
        3:list('BTW'),
        4:list('DRWTNQZJ'),
        5:list('FBHGLVTZ'),
        6:list('LPTCVBSG'),
        7:list('ZBRTWGP'),
        8:list('NGMTCJR'),
        9:list('LGBW')
    }
    for i in range(10,512):
        line=lines[i].split()
        a,b,c=int(line[1]),int(line[3]),int(line[5])
        add=''
        for j in range(a):
            add+=(d[b].pop())
        d[c]+=list(add[::-1])
    for i in range(1,10):
        ans+=d[i][-1]
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
