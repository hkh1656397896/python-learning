a,b,c=map(int,input("please input three numbers:").split(","))
if a**3+b**3+c**3>1000:
    print(a**3+b**3+c**3-1000)
else:
    print(a+b+c)

