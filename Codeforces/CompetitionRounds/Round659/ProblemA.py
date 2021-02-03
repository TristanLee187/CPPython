t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    
    ans=[]
    ans.append(200*'a')

    for i in range(n):
        if i==0:
            ans.append(l[0]*'a'+'b'+(200-l[0]-1)*'a')
        else:
            if l[i]>l[i-1]:
                ans.append(ans[-1][:l[i]]+'b'+(200-len(ans[-1][:l[i]])-1)*'a')
            else:
                point=ans[-1][l[i]]
                if point=='b':
                    ans.append(ans[-1][:l[i]]+'a'+(200-len(ans[-1][:l[i]])-1)*'a')
                else:
                    ans.append(ans[-1][:l[i]]+'b'+(200-len(ans[-1][:l[i]])-1)*'a')
    print('\n'.join(ans))
        
