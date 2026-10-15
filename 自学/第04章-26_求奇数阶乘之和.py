n=int(input())
x=2
term=1
t=1
if n==1:
    print("n=1,s=1")
else:
    for i in range(3,n+1,2):
        term*=(x*i)
        x+=2
        t+=term
    print(f"n={n},s={t}")

    