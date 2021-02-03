a,b,c=map(int,input().split())
k=int(input())

while b<=a and k>0:
    b*=2
    k-=1

while c<=b and k>0:
    c*=2
    k-=1

if b>a and c>b:
    print('Yes')
else:
    print('No')
