s=input()
w=25
h=6
l=(len(s)//w)//h

a=[]
for i in range(l):
    a.append(s[i*w*h:(i+1)*w*h])

image=''
for i in range(w*h):
    col=[a[j][i] for j in range(l)]
    flag=False
    for j in col:
        if j=='1':
            image+=j
            flag = True
            break
        elif j=='0':
            image+=' '
            flag=True
            break
    if not flag:
        image+=' '

for i in range(h):
    print(image[i*w:(i+1)*w])
