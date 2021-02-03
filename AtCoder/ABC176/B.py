n=int(input())
s=0
for i in str(n):
    s+=int(i)
while s>10000:
    a=0
    for i in str(s):
        a+=int(i)
    s=a
if s%9==0:
    print('Yes')
else:
    print('No')
