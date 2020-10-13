l=list(map(int, input().split(' ')))
n=l[0]
k=l[1]
l=list(map(int, input().split(' ')))
buckets = n*[0]
i=0
while i<k:
    i+=1
    j=0
    while j<n:
        thing=l[j]
        for a in range(int(j-thing+0.5), int(j+thing+1.5)):
            if a>=0 and a<=n-1:
                buckets[a]+=1
        j+=1
    j=0
    while j<n:
        l[j]=buckets[j]
        buckets[j]=0
        j+=1
for i in l:
    print(i, end=' ')
        
        
