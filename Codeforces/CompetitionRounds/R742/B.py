from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7


# Python 3 Program to find
# XOR of numbers from 1 to n.

# Function to calculate xor
def computeXOR(n):
    # Modulus operator are expensive
    # on most of the computers. n & 3
    # will be equivalent to n % 4.

    # if n is multiple of 4
    if n % 4 == 0:
        return n

    # If n % 4 gives remainder 1
    if n % 4 == 1:
        return 1

    # If n%4 gives remainder 2
    if n % 4 == 2:
        return n + 1

    # If n%4 gives remainder 3
    return 0


for _ in range(rn()):
    a,b=rns()
    ans=a
    x=computeXOR(a-1)
    if x==b:
        pass
    elif x^b==a:
        ans+=2
    else:
        ans+=1
    print(ans)