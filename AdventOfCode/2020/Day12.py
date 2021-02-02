a=[]
for i in range(764):
    a.append(input())
x=10
y=1
x2=0
y2=0
dir='e'
dirs=['e','n','w','s']
for i in a:
    mag=int(i[1:])
    if i[0]=='L':
        turn=mag//90
        if turn==1:
            x,y=-y,x
        elif turn==2:
            x=-x
            y=-y
        elif turn==3:
            x, y = y, -x
    elif i[0]=='R':
        turn = mag // 90
        if turn == 1:
            x, y = y, -x
        elif turn == 2:
            x = -x
            y = -y
        elif turn == 3:
            x, y = -y, x

    elif i[0]=='F':
        x2+=mag*x
        y2+=mag*y
    elif i[0]=='N':
        y+=mag
    elif i[0]=='E':
        x+=mag
    elif i[0]=='W':
        x-=mag
    else:
        y-=mag
print(abs(x2)+abs(y2))
print(x,y)
