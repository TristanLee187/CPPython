prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
ll=100
s=rs().split(',')
s=list(map(int, s))
b=[]
for _ in range(ll):
    rs()
    board=[rl() for i in range(5)]
    b.append(board)
marks=[[[0 for i in range(5)] for j in range(5)] for k in range(ll)]
bb=[]
mul=0
index=0
c=0
seen=set()
for i in range(len(s)):
    num=s[i]
    for board in range(ll):
        for j in range(5):
            for k in range(5):
                if b[board][j][k]==num:
                    marks[board][j][k]=1
                    if (sum([marks[board][j][l] for l in range(5)])==5 or sum([marks[board][l][k] for l in range(5)])==5) and board not in seen:
                        c+=1
                        seen.add(board)
                        if c==ll:
                            bb=b[board]
                            mul=num
                            index=board
                            break
            if len(bb)>0:
                break
        if len(bb) > 0:
            break
    if len(bb) > 0:
        break
# print(bb)
# print(marks[index])
um=0
for i in range(5):
    for j in range(5):
        if marks[index][i][j]==0:
            um+=bb[i][j]

file.close()
ans=um*mul
print(ans)
