a,b,c=map(int,input("please input three numbers:").split(","))
if a==b==c:print("equilateral triangle")
elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("right triangle")
elif a+b>c and a+c>b and b+c>a:
    print("ordinary triangle")
else:print("false")

