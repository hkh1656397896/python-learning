def Prime(p):
    if p<=1:return False
    elif p==2:return True
    else:
        for i in range(2,int(p**0.5)+1):
            if p%i==0:
                return False
        else:
            return True
def PrimeSum(m,n):
    T=0
    for i in range(m,n+1):
        if Prime(i)==True:
            T+=i
    return T
m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))
