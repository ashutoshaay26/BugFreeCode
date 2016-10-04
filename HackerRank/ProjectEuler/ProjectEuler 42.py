import math
t=int(input())
for i in range(t):
	N=int(input())
	n=(math.sqrt(1+8*N)-1)/2 # if  (math.sqrt(1+8*N)-1)/2 is integer then answer is index of triangle number 
	if (n%1) == 0:
		print(int(n))
	else:
		print('-1')