t=int(input())
for i in range(t):
	n=int(input())
	s=n*(n+1)//2
	sq=1
	for j in range(2,n+1):
		sq+=(j*j)
	print(abs(sq-s))
