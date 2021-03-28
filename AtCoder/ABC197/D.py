rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))
from math import dist, cos, sin, radians
n=rn()
x0,y0=rns()
x2,y2=rns()
cx=(x0+x2)/2
cy=(y0+y2)/2
theta=radians(360/n)

x1=(x0-cx)*cos(theta)-(y0-cy)*sin(theta)+cx
y1=(y0-cy)*cos(theta)+(x0-cx)*sin(theta)+cy
print(x1,y1)
