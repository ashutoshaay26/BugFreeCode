import math
def prime(num):
	last=-1
	while(num%2==0):
		last=2
		num=num//2
	s=int(math.sqrt(num))
	for j in range(3,s+1):
		while(num%j==0):
			last=j
			num=num//j
		j+=2
	if num>2:
		last=num
	return last


t=int(input())
for i in range(t):
	n=int(input())
	print(prime(n))