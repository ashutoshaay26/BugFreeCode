t=int(input())
for q in range(0,t):
	n,k = list(map(int, input().split()))
	s=list(input())
	ans=-1
	i=0
	prev=0
	ahead=k
	while ahead!=n:
		current=1
		for i in range(prev,ahead):
			current*=s[i]
		ans=max(current,ans)
		ahead+=1
		prev+=1
	print(ans)