rules={}
for i in range(131):
    l=input().split()
    rules[int(l[0][:-1])]=[[]]
    for i in l[1:]:
        if i=='|':
            rules[int(l[0][:-1])].append([])
        elif i=="\"a\"" or i=="\"b\"":
            rules[int(l[0][:-1])].append(i)
        else:
            rules[int(l[0][:-1])][-1].append(int(i))
input()
messages=[]
for i in range(502):
    messages.append(input())

def eval(num,rules):
    if len(rules[num])==1:
        return [rules[num][0]]
