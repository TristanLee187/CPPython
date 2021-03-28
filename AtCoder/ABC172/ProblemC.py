n,m,k = map(int, input().split(' '))

a=list(map(int, input().split(' ')))
b=list(map(int, input().split(' ')))

ans=0

asums = [0]
asum=0
for i in a:
    asum+=i
    asums.append(asum)

bsums = [0]
bsum=0
for i in b:
    bsum+=i
    bsums.append(bsum)


j=m

i=0

while i<len(asums) and k>=asums[i]:
    while k-asums[i]<bsums[j]:
        j-=1
    ans = max(ans, i+j)
    i+=1
print(ans)
    


    
        
    
