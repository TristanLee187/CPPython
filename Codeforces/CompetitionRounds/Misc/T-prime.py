def num(x):
    ans=2
    for i in range(2,int(x**0.5)+1):
        if x%i==0 and i!=x**0.5:
            return False
        elif i==x**0.5:
            ans+=1
    if ans==3:
        return True

n=int(input())
l=list(map(int, input().split(' ')))

for i in l:
    if num(i):
        print("YES")
    else:
        print('NO')
