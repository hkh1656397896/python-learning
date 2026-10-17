m=eval(input())
def weighted(x,k):
    if isinstance(x,int):
        return k
    elif isinstance(x,list):
        T=0
        for i in x:
            T+=weighted(i,k+1)
        return T
print(weighted(m,0))