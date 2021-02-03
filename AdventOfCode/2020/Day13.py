n=int(input())
a=[]
s=input().split(',')
for i in range(len(s)):
    if s[i]!='x':
        a.append([int(s[i]),i])
print([i[0] for i in a])
print([i[1] for i in a])
b=[]
for i in a:
    b.append(0)
    while (b[-1]*i[0]-i[1])%17!=0:
        b[-1]+=1
print(b)