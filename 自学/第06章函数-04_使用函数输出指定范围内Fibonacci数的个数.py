def fib(n):
    if n==0 or n==1:
        return 1
    else:
        a,b=1,1
        for _ in range(n-1):
            a,b=b,a+b
    return b
def PrintFN(m,n):
    T=[]
    a,b=1,1
    while a<=n:
        if a>=m:
            T.append(a)
        a,b=b,a+b
    return T
m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
b=fib(i)
print("fib({0}) = {1}".format(i,b))
fiblist=PrintFN(m,n)
print(len(fiblist))
