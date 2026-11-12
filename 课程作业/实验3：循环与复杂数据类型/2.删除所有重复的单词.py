line=list(input().split())
l=[]
for c in line:
    if c not in l:
        l.append(c)
l.sort()
for k in l:
    print(k,end=" ")
