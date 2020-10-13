l = list(map(int, input().split(' ')))
n = l[0]
k = l[1]
l = list(map(int, input().split(' ')))
index = l[0]-1
e = l[index]-1
lindex = [0]
count=k-1
while True and count>0:
    count-=1
    lindex += [index]
    if lindex.index(index)!=len(lindex)-1-lindex[::-1].index(index):
        break
    index = e
    e = l[index]-1
tloopsize = len(lindex)-lindex[::-1].index(index)-1-lindex.index(index)
k = k%tloopsize
if count==0:
    print(index+1)
else:
    print(l[lindex[k-1]])    
    
