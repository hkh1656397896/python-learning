def Reverse(s):
    s=int(str(s)[::-1])
    return s

def IsPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=int(input())
L=[]
if (n<=1) or (not isinstance(n,int)):
    print("error")
else:
    for i in range(2,n+1):
        if IsPrime(i) and IsPrime(Reverse(i)):
            L.append(str(i))
    k=" ".join(L)
    print(k)
