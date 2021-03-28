t=int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    n=l[0]
    k=l[1]
    i=(-1+(1+8*k)**0.5)/2
    if i%1!=0:
        i = int(i+1)
    else:
        i = int(i)
    
    j = k-((i-1)*i)//2-1
    
    ans = (n-i-1)*'a' + 'b' + (i-j-1)*'a' + 'b' + j*'a'
    print(ans)

