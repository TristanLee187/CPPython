"""
ID: tristan16
LANG: PYTHON3
PROB: combo
"""

a=open('combo.in','r')
b=open('combo.out','w')

n=int(a.readline())
farm=list(map(int,a.readline().split()))
mas=list(map(int,a.readline().split()))

combos=[]
for i in range(farm[0]-2,farm[0]+3):
    for j in range(farm[1] - 2, farm[1] + 3):
        for k in range(farm[2] - 2, farm[2] + 3):
            if [i%n,j%n,k%n] not in combos:
                combos.append([i%n,j%n,k%n])
ans=len(combos)*2
for i in combos:
    d1 = min(abs(i[0] - mas[0]), abs(n - max(i[0], mas[0]) + min(i[0], mas[0])))
    d2 = min(abs(i[1] - mas[1]), abs(n - max(i[1], mas[1]) + min(i[1], mas[1])))
    d3 = min(abs(i[2] - mas[2]), abs(n - max(i[2], mas[2]) + min(i[2], mas[2])))
    if d1 <= 2 and d2 <= 2 and d3 <= 2:
        ans -= 1





b.write(str(ans)+'\n')

a.close()
b.close()
