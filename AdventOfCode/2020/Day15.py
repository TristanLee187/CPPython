a=[0,1,5,10,3,12,19]
count=len(a)+1
last=0
d={a[i]:[i+1] for i in range(len(a))}
d[0].append(count)
print(d)
while count<30000000:
    count+=1
    if last in d and len(d[last])>1:
        last=d[last][-1]-d[last][-2]
        if last in d:
            d[last].append(count)
        else:
            d[last]=[count]
    else:
        last=0
        d[0].append(count)
print(last)