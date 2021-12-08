from itertools import permutations

prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
n=200
numtostring={
    0: {'a', 'b','c','e','f','g'},
    1:{'c','f'},
    2:{'a','c','d','e','g'},
    3:{'a','c','d','f','g'},
    4:{'b','d','c','f'},
    5:{'a','b','d','f','g'},
    6:{'a','b','d','e','f','g'},
    7:{'a','c','f'},
    8:{'a','b','c','d','e','f','g'},
    9:{'a','b','c','d','f','g'}
}
perms = list(permutations('abcdefg'))
print(perms[0], len(perms))

ss='abcdefg'
for i in range(n):
    s=rs().split()
    for perm in perms:
        nums = set()
        stringtonum={}
        ma = {ss[k]:perm[k] for k in range(7)}
        for j in range(10):
            word=''
            for k in range(len(s[j])):
                word+=ma[s[j][k]]
            # print('word: '+word)
            for num in numtostring:
                if numtostring[num] == set(word):
                    # print('!')
                    nums.add(num)
                    stringtonum[s[j]]=num
        if len(nums)==10:
            # print('?')
            dis=s[11:15]
            num=''
            for k in range(4):
                for string in stringtonum:
                    if set(string) == set(dis[k]):
                        num+=str(stringtonum[string])
                        break
            ans+=int(num)
            break


file.close()

print(ans)
