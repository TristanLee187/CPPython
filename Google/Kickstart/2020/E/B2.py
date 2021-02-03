t = int(input())
for _ in range(t):
    n,a,b,c=map(int,input().split())
    ans=0
    if b-c+a>n or (n>1 and a==b==c==1):
        ans='IMPOSSIBLE'
    else:
        ans=n*[1]
        pre=a-c
        suf=b-c
        
        for i in range(pre+1):
            if i==pre and b!=1:
                ans[i]=n
            elif i!=pre:
                if n>2:
                    ans[i]=2
                else:
                    ans[i]=1
        for i in range(n-suf-(c-1)-(b==1),n):
            if i<n-suf:
                ans[i]=n
            else:
                if n>2:
                    ans[i]=2
                else:
                    ans[i]=1
        

        ans=' '.join(list(map(str,ans)))



    print('Case #' + str(_ + 1) + ': ' + str(ans))
