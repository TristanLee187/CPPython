a=[0]
for i in range(112):
    a.append(int(input()))
a.sort()
diff=[]
for i in range(1,len(a)):
    diff.append(a[i]-a[i-1])
print(diff)
b=[0]
for i in diff:
    if i==1:
        b[-1]+=1
    else:
        b.append(0)
b=[i for i in b if i!=0]
print(b)
ans=1
for i in b:
    if i==1:
        ans*=1
    elif i==2:
        ans*=2
    elif i==3:
        ans*=4
    else:
        ans*=7
print(ans)