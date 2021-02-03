t=int(input())
count=0
while count<t:
    count+=1
    l = []
    n = int(input())
    for i in range(n):
        l.append(input())
    ud = 0
    lr = 0
    ans = True
    while ud<n-1:
        lr=0
        while lr<n-1:
            if l[ud][lr]=="1":
                if l[ud+1][lr]!="1" and l[ud][lr+1]!="1":
                    ans=False
                    break
            lr+=1
        ud+=1
    if ans:
        print("YES")
    else:
        print("NO")
                    
    
