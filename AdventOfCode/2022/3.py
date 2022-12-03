file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    for line in lines:
        n=len(line)
        first,second = line[:n//2], line[n//2:]
        for c in first:
            if c in second:
                if c.lower() == c:
                    add = ord(c) - ord('a') + 1
                else:
                    add = ord(c) - ord('A') + 27
                ans += add
                break
    return ans


# part 2
def part_2():
    ans = 0
    for i in range(0,300,3):
        group = lines[i:i+3]
        for c in group[0]:
            if c in group[1] and c in group[2]:
                if c.lower() == c:
                    add = ord(c) - ord('a') + 1
                else:
                    add = ord(c) - ord('A') + 27
                ans += add
                break
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
