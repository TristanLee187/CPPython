prob = "consecutive_cuts_chapter_1_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

#
# Read input
ans = ''
for t in range(rn()):
    pans=''
    n,k=rns()
    a=rl()
    b=rl()
    i = a.index(b[0])
    newa = a[i:] + a[:i]
    if a==b and k==1:
        pans='NO'
    elif a==b and k==0:
        pans='YES'
    elif n==2:
        pans='YES' if k%2==(0 if a==b else 1) else 'NO'
    elif newa==b and k>0:
        pans='YES'
    else:
        pans='NO'
    ans+='Case #{}: {}'.format(t+1, pans)
    ans+='\n'
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
