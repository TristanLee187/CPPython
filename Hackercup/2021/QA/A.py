prob="consistency_chapter_1_input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

#
#Read input
t=rn()
tests=[]
for _ in range(t):
    tests.append(rs())
#
file.close()

#CODE
ans=''
vowels=['A','E','I','O','U']

for _ in range(t):
    test=tests[_]
    pans=float('inf')
    for char in list(map(chr, range(65,91))):
        poss=0
        for c in test:
            if c==char:
                pass
            elif (c in vowels) == (char in vowels):
                poss+=2
            else:
                poss+=1
        pans=min(pans,poss)
    ans+='Case #{}: {}'.format(_+1, pans)
    if _<t-1:
        ans+='\n'
#

file=open(prob+".out","w")
file.write(str(ans))
file.close()
