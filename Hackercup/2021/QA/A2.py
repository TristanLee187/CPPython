prob="consistency_chapter_2_input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()
from collections import defaultdict

#
#Read input
ans=''
file2=open(prob+".out","w")


def bfs(char, d, seen, depth,wd):
    next=[]
    for char2 in d[char]:
        if char2 not in seen or seen[char2]>depth:
            seen[char2]=depth
            next.append(char2)
    for c in next:
        bfs(c,d,seen,depth+1,wd+1)


for t in range(rn()):
    s=rs()
    k=rn()
    re=defaultdict(list)
    for _ in range(k):
        a=rs()
        re[a[1]].append(a[0])
    # print(re)
    pans=float('inf')
    chose=''
    for char in list(map(chr, range(65, 91))):
        poss=0
        seen={char:0}
        flag=True
        bfs(char,re,seen,0,0)
        for c in s:
            if c==char:
                pass
            elif c not in seen:
                flag=False
                break
            else:
                poss+=seen[c]+1
        # print(char,seen)
        if flag:
            pans=min(pans,poss)
            if poss==pans:
                chose=char
    if pans==float('inf'):
        pans=-1
    file2.write('Case #{}: {}\n'.format(t+1, pans))

#
file.close()
file2.close()
