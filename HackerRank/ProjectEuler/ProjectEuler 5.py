def prime(m,n):
	while n%m!=0:
		r=n%m
		n=m
		m=r
	return m

t=int(input())
for i in range(t):
	n=int(input())
	ans=1
	for j in range(1,n+1):
		if ans%j!=0:
			ans*=(j//prime(min(ans,j),max(ans,j)))
	print(ans)
