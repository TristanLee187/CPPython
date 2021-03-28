n,k=map(int, input().split(' '))
l=list(map(int, input().split(' ')))
s=0
for i in range(k):
    m=min(l)
    s+=m
    l.pop(l.index(m))
print(s)
