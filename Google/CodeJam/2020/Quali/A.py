for _ in range(int(input())):
    n=int(input())
    m=[]
    for i in range(n):
        m.append(list(map(int,input().split())))
    ans1=0
    for i in range(n):
        ans1+=m[i][i]
    ans2=0
    for i in m:
        ans2+=(len(set(i))!=len(i))
    ans3=0
    for i in range(n):
        a=[j[i] for j in m]
        ans3+=(len(set(a))!=len(a))
    print('Case #' + str(_ + 1) + ':', ans1, ans2, ans3)