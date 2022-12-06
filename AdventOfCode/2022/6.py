file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    line=lines[0]
    for i in range(len(line)):
        block=line[i:i+4]
        if len(set(block))==4:
            return i+4


# part 2
def part_2():
    line=lines[0]
    for i in range(len(line)):
        block=line[i:i+14]
        if len(set(block))==14:
            return i+14


if __name__ == '__main__':
    print(part_1())
    print(part_2())
