rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')

for _ in range(rn()):
    n,l=rns()
    a=rl()
    posa=[0]
    posa+=a
    posa.append(l)
    posb=[0]
    posb+=[l-i for i in a[::-1]]
    posb.append(l)

    timea=[0]
    for i in range(1,n+2):
        timea.append((posa[i]-posa[i-1])/i+timea[-1])
    timeb=[0]
    for i in range(1,n+2):
        timeb.append((posb[i]-posb[i-1])/i+timeb[-1])
    ans=0
    j=0
    print(posa)
    print(timea)
    print(posb)
    print(timeb)
    if timea[1]>timeb[-1]:
        for i in range(1, n + 2):
            t = timeb[i]
            while j < len(timea) and timea[j] < t:
                j += 1
            s = posb[i] + posa[j - 1] + (t - timea[j - 1]) * j
            if s >= l:
                ans = t
                ans -= (s - l) / (i + j)
                break
    else:
        for i in range(1,n+2):
            t=timea[i]
            while j<len(timeb) and timeb[j]<t:
                j+=1
            s=posa[i]+posb[j-1]+(t-timeb[j-1])*j
            if s>=l:
                ans=t
                ans-=(s-l)/(i+j)
                break
    print(ans)
