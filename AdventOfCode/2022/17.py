file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    gas = lines[0]
    gas_p = 0
    rocks = [['####'], ['.#.', '###', '.#.'], ['..#', '..#', '###'], ['#', '#', '#', '#'], ['##', '##']]
    shaft = []
    for i in range(8088):
        shaft.append(['.' for j in range(7)])
    shaft.append(['#' for j in range(7)])
    curr_depth = len(shaft) - 1
    for i in range(2022):
        rock = rocks[i % 5][::-1]
        coors = [curr_depth - 4, 2]
        while True:
            prev_col = coors[1]
            if gas[gas_p] == '>':
                coors[1] = min(coors[1] + 1, 7 - len(rock[0]))
            else:
                coors[1] = max(0, coors[1] - 1)
            gas_p += 1
            gas_p %= len(gas)
            flag = any([shaft[coors[0] - r][coors[1] + c] == rock[r][c] == '#'
                        for r in range(len(rock)) for c in range(len(rock[0]))])
            if flag:
                coors[1] = prev_col
            coors[0] += 1
            flag = any([shaft[coors[0] - r][coors[1] + c] == rock[r][c] == '#'
                        for r in range(len(rock)) for c in range(len(rock[0]))])
            if flag:
                coors[0] -= 1
                break
        for r in range(len(rock)):
            for c in range(len(rock[0])):
                if rock[r][c] == '#':
                    shaft[coors[0] - r][coors[1] + c] = rock[r][c]
        curr_depth = min(curr_depth, coors[0] - len(rock) + 1)

    ans = len(shaft) - curr_depth - 1
    return ans


# part 2
def part_2():
    ans = 0

    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
