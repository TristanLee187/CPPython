t = int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ans=''
    for i in s:
        if i=='S':
            ans+='E'
        else:
            ans+='S'

    print('Case #' + str(_ + 1) + ': ' + ans)

