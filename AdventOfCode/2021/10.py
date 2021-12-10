prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
n=90
points={')':3, ']':57, '}':1197, '>':25137}
points2={'(':1, '[':2, '{':3, '<':4}
def match(a,b):
    symbs={'(':0, ')':0, '{':1, '}':1, '[':2, ']':2, '<':3, '>':3}
    return symbs[a]==symbs[b]
goodlines = []
for i in range(n):
    stack=[]
    s=rs()
    for j in range(len(s)):
        if s[j] in ['(','[','{','<']:
            stack.append(s[j])
        elif not match(stack[-1],s[j]):
            ans += points[s[j]]
            break
        else:
            stack.pop()
        if j==len(s)-1:
            goodlines.append(s)

file.close()


scores=[]
for line in goodlines:
    stack=[]
    for j in range(len(line)):
        if line[j] in ['(','[','{','<']:
            stack.append(line[j])
        else:
            stack.pop()
    stack.reverse()
    score=0
    for j in range(len(stack)):
        score*=5
        score += points2[stack[j]]
    scores.append(score)
scores.sort()
print(ans)
print(scores[len(scores)//2])
