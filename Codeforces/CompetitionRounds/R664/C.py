n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))


def solve(a,b,n,m):
    for d in range(2**9):
        temp=2**9-1
        tfound=True
        for i in range(n):
            found=False
            for j in range(m):
                if (a[i]&b[j])|d==d:
                    found=True
                    break
            
            if not found:
                tfound=False
                break
        if tfound:
            return d
    return 2**9-1

print(solve(a,b,n,m))
                
