file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    for line in lines:
        nums=[c for c in line if c.isnumeric()]
        ans += int(nums[0]+nums[-1])
    return ans


# part 2
def part_2():
    ans = 0
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for line in lines:
        a = []
        for c in range(len(line)):
            if line[c].isnumeric():
                a.append(line[c])
            else:
                for i in range(9):
                    num=nums[i]
                    if line[c:c+len(num)]==num:
                        a.append(str(i+1))
        ans += int(a[0]+a[-1])
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())