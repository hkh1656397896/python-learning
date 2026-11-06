def fact(n):
    jiecheng=1
    for i in range(1,n+1):
        jiecheng*=i
    return jiecheng

m=int(input())
print(fact(m))
