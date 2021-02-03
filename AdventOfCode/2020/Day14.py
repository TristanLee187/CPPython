a=[]
for i in range(572):
    a.append(input())
mask=''
memory={}
def masking(mask,num):
    binary=bin(num)[2:]
    binary=(36-len(binary))*'0'+binary
    ans=[]
    for i in range(36):
        if mask[i]=='X' or mask[i]=='1':
            ans+=[mask[i]]
        else:
            ans+=[binary[i]]
    base=0
    for i in range(36):
        if ans[35-i]=='1':
            base+=2**i*int(ans[35-i])
    rans=[base]
    Xs=[]
    for i in range(36):
        if ans[i]=='X':
            Xs.append(35-i)
    from itertools import combinations
    combos=[]
    for i in range(1,len(Xs)+1):
        combos+=list(combinations(Xs,i))
    for i in combos:
        add=0
        for j in i:
            add+=2**j
        rans.append(base+add)
    return rans
for i in a:
    if 'mask' in i:
        mask=i.split()[-1]
    else:
        index=int(i[i.index('[')+1:i.index(']')])
        num=int(i.split()[-1])
        l=masking(mask,index)
        for j in l:
            memory[j]=num
ans=0
for i in memory:
    ans+=memory[i]
print(ans)