m=set(map(int,input("numbers:").split(",")))
M=sorted(m)
L=[]
for i in M:
    if 9-i in M and i<9-i:
        L.append((i,9-i))
print(L)
