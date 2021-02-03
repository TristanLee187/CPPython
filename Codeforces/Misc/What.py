t=int(input())
 
for _ in range(t):
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	s={a[i]%k:0 for i in range(n)}
	for i in a:
		if i%k==0:continue
		s[i%k]+=1
	x=0
	for i in s.keys():
		x=max(x,s[i]*k-i)
	print(s)
	print(x+1 if x!=0 else 0)
