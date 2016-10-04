t=int(input())
for i in range(t):
	n=int(input())
	sp=1
	fp=2
	ans=2
	if n<1:
		ans=0
	else:
		for j in range(2,n-1):
			term=sp+fp
			sp=fp
			fp=term
			if term%2==0 and term<=n:
				ans+=term
			if term>n:
				break
	print(ans)