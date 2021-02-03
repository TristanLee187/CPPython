n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort()
def solve(l):
    ans=0
    for i in range(1,len(l)):
        if l[i][1]<l[i-1][1] and l[i][0]!=l[i-1][0]:
            return l[-1][0]
    return l[-1][1]
print(solve(l))