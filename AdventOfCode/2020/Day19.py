from collections import defaultdict

prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
rules=defaultdict(list)
for _ in range(131):
    s=rs().split()
    rule=int(s[0][:-1])
    if '|' not in s:
        if len(s)==2:
            if s[1] in ['"a"','"b"']:
                rules[rule].append([s[1][1]])
            else:
                rules[rule].append([int(s[1])])
        elif len(s)==3:
            rules[rule].append([int(s[1]), int(s[2])])
    else:
        if len(s)==4:
            rules[rule].append([int(s[1]), int(s[3])])
        else:
            rules[rule].append([int(s[1]), int(s[2])])
            rules[rule].append([int(s[4]), int(s[5])])

rs()




file.close()

print(ans)
for num in rules:
    print(num,rules[num])

