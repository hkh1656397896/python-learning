def fn(x,n):
    T=0
    for i in range(1,n+1):
        T+=int(str(x)*i)
    return T
a,b=input().split()
s=fn(int(a),int(b))
print(s)
