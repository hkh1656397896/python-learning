m=set(map(int,input().split(',')))
team2=[6,7,8,9,10]
L=[]
for x in team2:
    if x not in m:
        L.append(x)
print(*L)
        
