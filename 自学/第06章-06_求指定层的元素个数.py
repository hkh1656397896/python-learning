m=eval(input())
n=int(input())
def f(x,k):
    if isinstance(x,int) and n==k:
        return 1
    elif isinstance(x,list):
        T=0
        for i in x:
            T+=f(i,k+1)
        return T
    else:return 0
print(f(m,0))
