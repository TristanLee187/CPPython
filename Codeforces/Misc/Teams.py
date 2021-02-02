i = int(input())
count=0
ans=0
while count<i:
    count+=1
    l = list(map(int, input().split(' ')))
    if sum(l)>1:
        ans+=1
print(ans)
