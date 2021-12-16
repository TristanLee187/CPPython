file=open("input.txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
hexes={}
for i in range(10):
    add=bin(i)[2:]
    while len(add)<4:
        add='0'+add
    hexes[str(i)]=add
for i in range(6):
    hexes[['A','B','C','D','E','F'][i]] = bin(10+i)[2:]
hexmess=rs()
mess=''
for c in hexmess:
    mess+=hexes[c]
def bintonum(string):
    ans=0
    for i in range(len(string)):
        if string[i]=='1':
            ans+=2**(len(string)-i-1)
    return ans
def solve(string, p):
    vers=bintonum(string[p:p + 3])
    t=bintonum(string[p + 3:p + 6])
    p+=6
    value = 0
    if t==4:
        value=''
        while string[p]== '1':
            value+= string[p + 1:p + 5]
            p+=5
        value += string[p + 1:p + 5]
        p += 5
        return [vers, bintonum(value), p]
    typeid=string[p]
    p+=1
    if typeid=='0':
        vals=[]
        subpacklength = bintonum(string[p:p + 15])
        p+=15
        ans=solve(string, p)
        vals.append(ans[1])
        vers+=ans[0]
        while ans[2]<p+subpacklength:
            ans=solve(string, ans[2])
            vals.append(ans[1])
            vers+=ans[0]

        p=ans[2]
    else:
        vals=[]
        numsubpack=bintonum(string[p:p + 11])
        p+=11
        while numsubpack:
            numsubpack-=1
            ans=solve(string, p)
            vals.append(ans[1])
            p=ans[2]
            vers+=ans[0]
    if t==0:
        value=sum(vals)
    if t==1:
        prod=1
        for num in vals:
            prod*=num
        value=prod
    if t==2:
        value=min(vals)
    if t==3:
        value=max(vals)
    if t==5:
        value = 1 if vals[0]>vals[1] else 0
    if t==6:
        value = 1 if vals[0]<vals[1] else 0
    if t==7:
        value=1 if vals[0]==vals[1] else 0
    return [vers, value, p]

file.close()
ans=solve(mess, 0)
print(ans)
