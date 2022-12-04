file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    for line in lines:
        l,r=line.split(',')
        a,b=list(map(int,l.split('-')))
        c,d=list(map(int,r.split('-')))
        if (a<=c and b >= d) or (c<=a and d >= b):
            ans+=1

    return ans


# part 2
def part_2():
    ans = 0
    for line in lines:
        l,r=line.split(',')
        a,b=list(map(int,l.split('-')))
        c,d=list(map(int,r.split('-')))
        if a <= d and c <= b:
            ans+=1
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
