a=[]
d={}
for i in range(594):
    a.append(input())

colors={}
for i in a:
    colors[i.split('bags')[0][:-1]]=' '.join(i.split()[4:])

def solve(color, colors):
    l=colors[color]
    a=[]
    c=[]
    if 'no' in l:
        return 0
    if l!='.':
        b=l.split()
        for k in range(len(b)):
            if b[k] in ['bag', 'bag,', 'bag.', 'bags', 'bags,', 'bags.']:
                a.append(b[k - 2] + ' ' + b[k - 1])
                c.append(int(b[k-3]))
    ans=sum(c)
    for i in range(len(a)):
        ans+=c[i]*solve(a[i],colors)
    print(color,ans)
    return ans

print(solve('shiny gold', colors))
