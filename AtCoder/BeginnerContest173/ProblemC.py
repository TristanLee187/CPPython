h,w,k=map(int,input().split(' '))
d=[]
for i in range(h):
    d.append(input())

rbits=[]
for i in range(2**h):
    s=bin(i)
    s=s[s.index('b')+1:]
    s=(h-len(s))*'0'+s
    rbits.append(s)

cbits=[]
for i in range(2**w):
    s=bin(i)
    s=s[s.index('b')+1:]
    s=(w-len(s))*'0'+s
    cbits.append(s)


    
ans=0


for i in rbits:
    for j in cbits:
        a=0
        for c in range(h):
            if i[c]=='1':
                for e in range(w):
                    if j[e]=='1' and d[c][e]=='#':
                        a+=1
        if a==k:
            ans+=1

print(ans)




