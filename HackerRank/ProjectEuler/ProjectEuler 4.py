def find_max_palindrome(n):
    max_palindrome = 0
    a = 999
    while a > 99:
        b = 999
        while b >= a:
            prod = a*b
            if prod<n and prod > max_palindrome and str(prod)==(str(prod)[::-1]):
                max_palindrome = prod
            b -= 1
        a -= 1
    return max_palindrome
 
t=int(input())
for i in range(t):
	print(find_max_palindrome(int(input())))