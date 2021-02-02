import math

l=list(map(int, input().split(' ')))
a=l[0]
b=l[1]
h=l[2]
m=l[3]
hours = (h+m/60)/12
minutes = m/60
theta = 2*math.pi*(hours-minutes)
ans = a**2+b**2-2*a*b*math.cos(theta)
print(ans**0.5)
