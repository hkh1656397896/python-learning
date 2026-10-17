m=eval(input())
L=[]
def total(x):
    if isinstance(x,(int,float)):
        return x
    elif isinstance(x,(list,tuple)):
        T=0
        for i in x:
            T+=total(i)
        return T
    else:return 0
for n in m:
    L.append(total(n))
print(sum(L))


