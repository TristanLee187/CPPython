t=int(input())
count=0
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while count<t:
    count+=1
    l1 = list(map(int, input().split(' ')))
    n=l1[0]
    a=l1[1]
    b=l1[2]
    ans=''
    index=0
    while index<b:
        ans+=l[index]
        index+=1
    ans += (a-b)*l[index-1]
    while len(ans)<n:
        ans = 2*ans
    print(ans[:n])
    
