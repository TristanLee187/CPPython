file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


def f(x, y):
    if type(x) == type(y) == int:
        if x < y:
            return -1
        if x == y:
            return 0
        return 1
    if type(x) == type(y) == list:
        if not x and not y:
            return 0
        if not x:
            return -1
        if not y:
            return 1
        ans = f(x[0], y[0])
        if ans == -1:
            return -1
        if ans == 1:
            return 1
        return f(x[1:], y[1:])
    if type(x) == int:
        return f([x], y)
    if type(y) == int:
        return f(x, [y])


# part 1
def part_1():
    ans = 0
    c = 0
    for i in range(0, len(lines), 3):
        c += 1
        a = eval(lines[i])
        b = eval(lines[i + 1])
        if f(a, b) in [-1, 0]:
            # print(c)
            ans += c
    return ans


# part 2
def part_2():
    ans = 0
    a = [line for line in lines if line]
    a.append('[[2]]')
    a.append('[[6]]')
    a = [eval(line) for line in a]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if f(a[j], a[i]) == -1:
                a[i], a[j] = a[j], a[i]
    nums = []
    for i in range(len(a)):
        if a[i] in [[[2]], [[6]]]:
            nums.append(i + 1)
    return nums[0] * nums[1]


if __name__ == '__main__':
    print(part_1())
    print(part_2())
