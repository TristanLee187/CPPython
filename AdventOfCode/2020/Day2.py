ans=0
for i in range(1000):
    s=input()
    l=s.split()
    nums=list(map(int,l[0].split('-')))
    chars=[l[-1][nums[j]-1] for j in range(2)]
    if chars.count(l[1][0])==1:
        ans+=1
print(ans)