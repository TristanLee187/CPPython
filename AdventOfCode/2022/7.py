from collections import defaultdict

file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    ans = 0
    d=defaultdict(list)
    p=0
    dir_stack=[]
    while p<len(lines):
        line=lines[p].split()
        if line[1] == 'cd':
            curr_dir = line[2]
            if curr_dir == '..':
                dir_stack.pop()
            elif curr_dir == '/':
                dir_stack.clear()
                dir_stack.append('/')
            else:
                dir_stack.append(curr_dir)
            p+=1
        elif line[1] == 'ls':
            path = '-'.join(dir_stack)
            p+=1
            while p<len(lines) and lines[p][0]!='$':
                a,b=lines[p].split()
                if a.isnumeric():
                    d[path].append(int(a))
                else:
                    d[path].append(path + '-' + b)
                p+=1
    vals=defaultdict(int)
    def solve(directory):
        # print(directory)
        for thing in d[directory]:
            if type(thing) == int:
                vals[directory]+=thing
            else:
                vals[directory] += solve(thing)
        return vals[directory]
    solve('/')
    # print(vals)
    for key in vals:
        if vals[key]<=100000:
            ans+=vals[key]
    return ans


# part 2
def part_2():
    ans = float('inf')
    d=defaultdict(list)
    p=0
    dir_stack=[]
    while p<len(lines):
        line=lines[p].split()
        if line[1] == 'cd':
            curr_dir = line[2]
            if curr_dir == '..':
                dir_stack.pop()
            elif curr_dir == '/':
                dir_stack.clear()
                dir_stack.append('/')
            else:
                dir_stack.append(curr_dir)
            p+=1
        elif line[1] == 'ls':
            path = '-'.join(dir_stack)
            p+=1
            while p<len(lines) and lines[p][0]!='$':
                a,b=lines[p].split()
                if a.isnumeric():
                    d[path].append(int(a))
                else:
                    d[path].append(path + '-' + b)
                p+=1
    vals=defaultdict(int)
    def solve(directory):
        # print(directory)
        for thing in d[directory]:
            if type(thing) == int:
                vals[directory]+=thing
            else:
                vals[directory] += solve(thing)
        return vals[directory]
    solve('/')
    # print(vals)
    total=70000000
    need=30000000
    total_used = vals['/']
    # print(total_used)
    for v in vals.values():
        if need + total_used - v <=total:
            ans=min(ans, v)
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
