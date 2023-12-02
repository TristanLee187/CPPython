from collections import defaultdict

file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    for line in lines:
        g, games = line.split(':')
        gid = int(g.split()[1])
        flag = True

        for game in games.split(';'):
            cubes = game.split(',')
            for cube in cubes:
                num, color = cube.strip().split()
                num=int(num)
                if color=='red' and num>12:
                    flag=False
                if color=='blue' and num>14:
                    flag=False
                if color=='green' and num>13:
                    flag=False
        if flag:
            ans+=gid
    return ans


# part 2
def part_2():
    ans = 0
    for line in lines:
        g, games = line.split(':')
        gid = int(g.split()[1])
        d=defaultdict(int)
        for game in games.split(';'):
            cubes = game.split(',')
            for cube in cubes:
                num, color = cube.strip().split()
                num=int(num)
                d[color] =max(d[color], num)
        ans += d['red']*d['blue']*d['green']
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())