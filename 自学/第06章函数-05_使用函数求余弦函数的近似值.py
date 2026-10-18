def funcos(eps,x):
    sign=-1
    T=i=e=m=1
    j=2
    while abs(e)>=eps:
        m*=(i*j)
        e=(x**j)/m*sign
        i+=2
        j+=2
        sign=-sign
        if abs(e)<eps:break
        T+=e
    return T
eps,x=input().split()
eps,x=float(eps),float(x)
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))
