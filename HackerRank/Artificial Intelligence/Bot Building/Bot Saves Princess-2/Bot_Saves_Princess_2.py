sx=0
tx=0
ty=0
sy=0  
#print all the moves here
m = int(input())
d=input().strip().split()
for i in range(0,m):
    grid=[]
    grid = input().strip()
    for j in range(0,len(grid)):
        if grid[j]=='m':    #finding the index of source
            sx=i
            sy=j
        elif grid[j]=='p':  #finding the index of destination
            tx=i
            ty=j
if tx<sx:
    print('UP')				#move upward till both stand on same x axis		
    sx=sx-1
elif tx>sx:
    print('DOWN')           #move upward till both stand on same x axis
    sx=sx+1
elif ty<sy:
    print('LEFT')           #move upward till both stand on same y axis
    sy=sy-1
elif ty>sy:
    print('RIGHT')          #move upward till both stand on same y axis
    sy=sy+1