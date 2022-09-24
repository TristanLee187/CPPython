from collections import defaultdict

prob = "perfectly_balanced_chapter_1_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

#
# Read input
ans = ''
for t in range(rn()):
    pans=0
    s=rs()
    n=len(s)
    pre=[defaultdict(int)]
    d=defaultdict(int)
    for i in range(n):
        d[s[i]]+=1
        pre.append(d.copy())
    # print(pre)
    q=rn()
    for i in range(q):
        l,r=rns()
        add=0
        if (r-l)%2==0:
            mid=(r+l)//2
            left = {}
            for letter in pre[mid]:
                if pre[mid][letter] - pre[l-1][letter] != 0:
                    left[letter] = pre[mid][letter] - pre[l-1][letter]
            right={}
            for letter in pre[r]:
                if pre[r][letter] - pre[mid][letter] != 0:
                    right[letter] = pre[r][letter] - pre[mid][letter]
            for letter in left:
                left_c = left.copy()
                left_c[letter]-=1
                if left_c[letter]==0:
                    del left_c[letter]
                if left_c==right:
                    add=1

            mid-=1
            left = {}
            for letter in pre[mid]:
                if pre[mid][letter] - pre[l - 1][letter] != 0:
                    left[letter] = pre[mid][letter] - pre[l - 1][letter]
            right = {}
            for letter in pre[r]:
                if pre[r][letter] - pre[mid][letter] != 0:
                    right[letter] = pre[r][letter] - pre[mid][letter]
            # print(l,r)
            # print(left, right)
            for letter in right:
                left_c = right.copy()
                left_c[letter] -= 1
                if left_c[letter] == 0:
                    del left_c[letter]
                if left_c == left:
                    add = 1

        pans+=add
    ans+='Case #{}: {}'.format(t+1, pans)
    ans+='\n'
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
