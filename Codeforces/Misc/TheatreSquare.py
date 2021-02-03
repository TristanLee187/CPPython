l = list(map(int, input().split(' ')))
r = l[0]//l[2]
c = l[1]//l[2]
if l[0]%l[2]!=0:
    r+=1
if l[1]%l[2]!=0:
    c+=1
print(r*c)
