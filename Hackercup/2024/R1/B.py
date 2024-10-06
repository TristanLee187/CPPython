prob = "prime_subtractorization_input"

file = open(prob + ".txt")

rn = lambda: int(file.readline())
rns = lambda: map(int, file.readline().split())
rl = lambda: list(map(int, file.readline().split()))
rs = lambda: file.readline().strip()


# Precompute all answers
MAX_N = 10**7
is_prime = [True for _ in range(MAX_N+1)]
is_prime[0]=False
is_prime[1]=False
for p in range(2, len(is_prime)):
    if is_prime[p]:
        for i in range(2*p, len(is_prime), p):
            is_prime[i]=False

answers = [0 for _ in range(MAX_N+1)]
answers[5] = 2
for num in range(6, MAX_N+1):
    answers[num] = answers[num-1]
    if is_prime[num] and is_prime[num-2]:
        answers[num]+=1

#
# Read input
ans = ''
for t in range(rn()):
    pans=''
    n=rn()
    pans=answers[n]
    ans+='Case #{}: {}'.format(t+1, pans)
    ans+='\n'
#
file.close()

file = open(prob + ".out", "w")
file.write(str(ans))
file.close()
