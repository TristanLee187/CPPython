rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))


def ternary_search(f, left, right, absolute_precision):
    """Find maximum of unimodal function f() within [left, right]
    To find the minimum, reverse the if/else statement or reverse the comparison.
    """
    while abs(right - left) >= absolute_precision:
        left_third = left + (right - left) / 3
        right_third = right - (right - left) / 3

        if f(left_third) > f(right_third):
            left = left_third
        else:
            right = right_third

     # Left and right are the current bounds; the maximum is between them
    return (left + right) / 2

for _ in range(int(input())):
    ans = float('inf')
    w,n=rns()
    x=rl()
    def f(a):
        pos = 0
        for num in x:
            pos += min(abs(a - num), n - abs(a - num))
        return pos
    ans=ternary_search(f,0,max(x),1)

    print('Case #' + str(_ + 1) + ': ' + str(ans))