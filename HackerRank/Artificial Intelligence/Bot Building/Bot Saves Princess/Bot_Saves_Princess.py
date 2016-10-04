# Hello World program in Python
#!/usr/bin/python
sx=0
tx=0
ty=0
sy=0  
#print all the moves here
m = int(input())
for i in range(0,m):
    grid=[]
    grid = input().strip()
    for j in range(0,len(grid)):
        if grid[j]=='m':            #finding the index of source
            sx=i
            sy=j
        elif grid[j]=='p':			#finding the index of destination
            tx=i
            ty=j
if tx<sx:
        while sx>tx:               #move upward till both stand on same x axis
            print('UP')
            sx=sx-1
elif tx>sx:
        while sx!=tx:             #move upward till both stand on same x axis
            print('DOWN')
            sx=sx+1

if ty<sy:                           #move upward till both stand on same y axis
       while sy!=ty:
            print('LEFT')
            sy=sy-1
elif ty>sy:
        while sy!=ty:             #move upward till both stand on same y axis
            print('RIGHT')
            sy=sy+1
        

