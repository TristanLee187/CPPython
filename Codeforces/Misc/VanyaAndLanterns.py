n, l = map(int, input().split(' '))

L=list(map(int, input().split(' ')))
L=sorted(L)
ans=0
for i in range(1,len(L)):
    ans = max(ans, (L[i]-L[i-1])/2)

if L[0]!=0:
    ans = max(ans, L[0])

if L[-1]!=l:
    ans = max(ans, l-L[-1])

print(ans)

    
