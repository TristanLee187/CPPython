prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
n=1000
dd=12
st=[rs() for i in range(n)]

d=0
ds=st.copy()
for i in range(dd):
    newd=[]
    most=sum(map(int,[ds[j][i] for j in range(len(ds))]))
    if most>=len(ds)/2:
        most=1
    else:
        most=0
    newd = [s for s in ds if s[i]==str(most)]
    ds=newd.copy()
    if len(ds)==1:
        d=ds[0]
        break

e=0
es=st.copy()
for i in range(dd):
    newe=[]
    most=sum(map(int,[es[j][i] for j in range(len(es))]))
    if most>=len(es)/2:
        most=0
    else:
        most=1
    newe = [s for s in es if s[i]==str(most)]
    es=newe.copy()
    if len(es)==1:
        e=es[0]
        break
# print(es)
print(d,e)