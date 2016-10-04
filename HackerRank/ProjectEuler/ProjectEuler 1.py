t=int(input())
for i in range(t):
    n=int(input())
    three=(n-1)//3
    five=(n-1)//5
    fif=(n-1)//15
    ans=three*(6+(three-1)*3)+five*(10+(five-1)*5)-fif*(30+(fif-1)*15)
    print(ans//2)