t=int(input())
count=0
while count<t:
    count+=1
    l1 = list(map(int, input().split(' ')))
    l2 = list(map(int, input().split(' ')))

    add = min(l1)
    add2 = min(l2)

    target = max(l1)
    target2 = max(l2)

    if target==target2:
        if add+add2==target:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    
                
