n, k = map(int, input().split(' '))
l=list(map(int, input().split(' ')))
newl = [l[0]]
ans = 0
for i in range(n-1):
    if l[i]+l[i+1]<k:
        ans += k-l[i]-l[i+1]
        newl.append(k-l[i])
        l[i+1]=k-l[i]
    else:
        newl.append(l[i+1])

print(ans)

for i in newl[:-1]:
    print(i, end=' ')
print(newl[-1])
