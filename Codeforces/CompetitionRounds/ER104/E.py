rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))

n1,n2,n3,n4=rns()
a=rl()
b=rl()
c=rl()
d=rl()
m1=rn()
pairs1={}
for i in range(m1):
    p1,p2=rns()
    if p1 not in pairs1:
        pairs1[p1]=[]
    pairs1[p1].append(p2)
m2=rn()
pairs2={}
for i in range(m2):
    p1,p2=rns()
    if p1 not in pairs2:
        pairs2[p1]=[]
    pairs2[p1].append(p2)
m3=rn()
pairs3={}
for i in range(m3):
    p1,p2=rns()
    if p1 not in pairs3:
        pairs3[p1]=[]
    pairs3[p1].append(p2)

