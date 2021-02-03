t=int(input())
count=0
while count<t:
    count+=1
    n = int(input())
    ans = 0
    while n>0:
        ans += n//2 * (4*n-4)
        n-=2
    print(ans)
