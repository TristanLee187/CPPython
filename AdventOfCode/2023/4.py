from collections import defaultdict

file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    for line in lines:
        cards = line.split()
        wins = cards[2:12]
        mine = cards[13:]
        match = set(wins) & set(mine)
        if match:
            ans += 2**(len(match)-1)
    return ans


# part 2
def part_2():
    ans = 0
    counts=defaultdict(lambda: 1)
    scores=defaultdict(int)
    for i in range(len(lines)):
        line = lines[i]
        cards = line.split()
        wins = cards[2:12]
        mine = cards[13:]
        match = set(wins) & set(mine)
        # if match:
        #     scores[i] = 2**(len(match)-1)
        # else:
        #     scores[i]=0
        counts[i]
        for j in range(i+1,i+len(match)+1):
            counts[j]+=counts[i]
    for num in counts:
        ans += counts[num]
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())