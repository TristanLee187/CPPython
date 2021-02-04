from itertools import permutations

s=input()
letters=set()
for i in s:
    letters.add(i)
ans=float('inf')
perms = permutations(list(letters))
for perm in perms:
    curr=0
    last=0
    for i in s:
        if perm.index(i)<=last:
            last=0
            curr+=1
        else:
            last=perm.index(i)
    ans=min(ans,curr)
print(ans)