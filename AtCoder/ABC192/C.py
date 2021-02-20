rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n,k=rns()
ans=n
for i in range(k):
    a=''.join(sorted(list(str(ans))))
    b=''.join(sorted(list(str(ans)),reverse=True))
    ans=int(b)-int(a)
print(ans)