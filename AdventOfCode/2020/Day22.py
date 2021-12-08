from collections import deque

prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
rs()
deck1 = deque([rn() for i in range(25)])
rs()
rs()
deck2 = deque([rn() for i in range(25)])

file.close()

def solve(deck1, deck2):
    seen1=set()
    seen2=set()
    def move(win, lose):
        win.append(win.popleft())
        win.append(lose.popleft())
    while len(deck2)>0 and len(deck1)>0:
        if tuple(deck1) in seen1 and tuple(deck2) in seen2:
            return 1
        else:
            seen1.add(tuple(deck1))
            seen2.add(tuple(deck2))
            if deck1[0]<=len(deck1)-1 and deck2[0]<=len(deck2)-1:
                d1pop = deque()
                for i in range(deck1[0]):
                    d1pop.append(deck1[i+1])
                d2pop=deque()
                for i in range(deck2[0]):
                    d2pop.append(deck2[i+1])
                winner = solve(d1pop, d2pop)
                if winner==1:
                    move(deck1, deck2)
                else:
                    move(deck2, deck1)
            elif deck1[0]>deck2[0]:
                move(deck1, deck2)
            else:
                move(deck2, deck1)
    if len(deck1)==0:
        return 2
    return 1

solve(deck1, deck2)

win = deck1 if len(deck1)>0 else deck2

for i in range(1,len(win)+1):
    ans+=i*win.pop()
print(ans)
