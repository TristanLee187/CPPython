rules=[]
for i in range(20):
    a=input().split()
    b,c=map(int,a[-3].split('-'))
    d,e=map(int,a[-1].split('-'))
    rules.append([b,c,d,e])
junk=''
for i in range(2):
    junk+=input()
yours=l=list(map(int,input().split(',')))
for i in range(2):
    junk+=input()

total=[]
for i in range(237):
    l=list(map(int,input().split(',')))
    flag = True
    for k in range(len(l)):
        flag2=False
        for j in range(len(rules)):
            flag2 = flag2 or (rules[j][0]<=l[k]<=rules[j][1] or rules[j][2]<=l[k]<=rules[j][3])
        flag=flag and flag2
    if flag:
        total.append(l)

poss=[]
for i in range(len(rules)):
    poss.append([])

for i in range(len(total[0])):
    col=[total[j][i] for j in range(len(total))]
    for j in range(len(rules)):
        if all([(rules[j][0]<=k<=rules[j][1] or rules[j][2]<=k<=rules[j][3]) for k in col]):
            poss[j].append(i)

newrules=len(rules)*[-1]
while -1 in newrules:
    val=0
    rule=0
    for i in range(len(poss)):
        if len(poss[i])==1:
            val=poss[i][0]
            rule=i
            break
    for i in range(len(poss)):
        if val in poss[i]:
            poss[i].remove(val)
    newrules[rule]=val

print(newrules)
ans=1
for i in range(6):
    ans*=yours[newrules[i]]
print(ans)

#20,237