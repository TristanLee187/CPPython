file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    them = ['A', 'B', 'C']
    me = ['X', 'Y', 'Z']
    ans = 0
    for line in lines:
        a,b=line.split()
        ans+=me.index(b)+1
        if them.index(a) == me.index(b):
            ans += 3
        elif me.index(b) == (them.index(a)+1)%3:
            ans+=6
    return ans


# part 2
def part_2():
    them = ['A', 'B', 'C']
    me = ['X', 'Y', 'Z']
    ans = 0
    for line in lines:
        a,b=line.split()
        ans+=me.index(b)*3
        if b=='X':
            choice = (them.index(a)-1)%3
        elif b=='Y':
            choice = them.index(a)
        else:
            choice = (them.index(a)+1)%3
        ans += choice + 1
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
