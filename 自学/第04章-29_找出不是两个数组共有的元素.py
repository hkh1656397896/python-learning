m=list(map(int,input().split()))
n=list(map(int,input().split()))
L=[]
for a in m[1:m[0]+1]:
    if a not in n[1:n[0]+1] and a not in L:
        L.append(a)    
for b in n[1:n[0]+1]:
    if b not in m[1:m[0]+1] and b not in L:
        L.append(b)
print(*L)