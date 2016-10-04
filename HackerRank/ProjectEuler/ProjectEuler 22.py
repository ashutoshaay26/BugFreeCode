t=int(input())
a=[]
for i in range(0,t):
	b=input()
	a.append(b)
	a.sort()
n=int(input())
for j in range(0,n):
	s=input()
	print(sum(ord(i)-ord('A')+1 for i in s)*(a.index(s)+1))