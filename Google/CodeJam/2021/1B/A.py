from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
from itertools import permutations

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def pow(base, e, mod):
    return modinv(base, mod)

for _ in range(rn()):
    a,b,c=rns()
    tries = permutations([a,b,c])
    def solve():
        for tri in tries:
            sticks = tri[0]
            mticks = tri[1]
            hticks = tri[2]
            big = 720*60*10**9

            c = (60*mticks-sticks)%big
            c = [pow(59, -1, big)*(big-c)%big, -(pow(59, -1, big)*(big-c)%big)]

            c2 = (12*hticks-mticks)%big
            c2 = [pow(11,-1,big)*(big-c2)%big, -(pow(11,-1,big)*(big-c2)%big)]

            for d in c:
                for e in c2:
                    if d==e:
                        sns = (sticks+d) / 720
                        mns = (mticks+d) / 12
                        hns = hticks+e

                        if (mns-sns)%(60*10**9)==0 and (hns-mns)%(3600*10**9)==0:
                            h = int((hns-mns)//(3600*10**9))
                            m = int((mns-sns)//(60*10**9))
                            s = int(sns//(10**9))
                            m+=s//60
                            s%=60

                            h+=m//60
                            m%=60

                            h%=12

                            ns = int(sns%(10**9))

                            return '{} {} {} {}'.format(h, m, s, ns)
    ans=solve()
    print('Case #' + str(_+1)+': ' + str(ans))