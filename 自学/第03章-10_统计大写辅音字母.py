M=input()
HEX="BCDFGHJKLMNPQRSTVWXYZ"
L=[]
for i,ch in enumerate(M):
    if ch in HEX:
        L.append(1)
y=map(int,L)
x=sum(y)
print(x)
