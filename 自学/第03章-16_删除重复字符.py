m=input()
L=[]
for i in m:
    if i not in L:
        L.append(i)
y=sorted(L)
x="".join(y)
print(x)