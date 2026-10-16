m=int(input())
V=set()
E=[]
S=0
for _ in range(m):
    x=eval(input())
    for y,z in x.items():
        V.add(y)
        for v,w in z.items():
            S+=w
            E.append(v)
print(len(V),len(E),S)



