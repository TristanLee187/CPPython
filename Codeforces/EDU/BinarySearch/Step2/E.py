n=float(input())
lo=1
hi=n
while lo<hi-10**-6:
    mid=(lo+hi)/2
    acc=mid**2+mid**0.5
    if acc<n:
        lo=mid
    else:
        hi=mid
print(lo)