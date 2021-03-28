from decimal import *

n=int(input())
l=list(map(int, input().split(' ')))
q=int(input())
freqs=[]
add=Decimal(0)
for i in l:
    if i>=len(freqs):
        freqs+=(i-len(freqs)+1)*[0]
    freqs[i]+=1
    add+=i

        
for i in range(q):
    b,c=map(int, input().split(' '))
    if b<len(freqs):
        add+=Decimal((c-b)*(freqs[b]))
        if c>=len(freqs):
            freqs+=(c-len(freqs)+1)*[0]
        freqs[c]+=freqs[b]
        freqs[b]=0
    print(add)

    
