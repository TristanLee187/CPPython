prob = "weak_typing_chapter_1_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()

#
# Read input
ans = ''
for t in range(rn()):
    n=rn()
    w=rs()
    s=w.replace('F','')
    st=[]
    for sub in s:
        if len(st)==0:
            st.append(sub)
        elif sub!=st[-1]:
            st.append(sub)
    # print(st)
    ans+="Case #{}: ".format(t+1)+str(max(len(st)-1,0))+'\n'
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
