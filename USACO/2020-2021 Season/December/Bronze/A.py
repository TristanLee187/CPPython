l=list(map(int,input().split()))
l.sort()
a=l[0]
b=l[1]
c=l[-1]-a-b
print(a,b,c)