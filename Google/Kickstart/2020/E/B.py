t = int(input())
for _ in range(t):
    n,a,b,c=map(int,input().split())
    ans=0
    if b-c+a>n or (n>1 and a==b==c==1):
        ans='IMPOSSIBLE'
    else:
        ans=n*[1]
        if a==1:
            ans[0]=n
            for j in range(n-1,n-1-(b-c),-1):
                ans[j]=2
        elif b==1:
            ans[-1]=n
            for j in range(a-c):
                ans[j]=2
        else:
            for i in range(a-(not c==1)):
                if i>=a-c:
                    ans[i]=n
                else:
                    ans[i]=1
            for i in range(n-1,n-1-(b-c)-(not c==1),-1):
                if i==n-1-(b-c):
                    ans[i]=n
                else:
                    ans[i]=2
        ans=' '.join(list(map(str,ans)))
            
            
            


    

    print('Case #' + str(_ + 1) + ': ' + str(ans))
