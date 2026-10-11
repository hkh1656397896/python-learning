lower,upper=map(int,input().split())
F=lower
if 1<=lower<=upper<=100:
    print("fahr celsius")
    for i in range(0,upper-lower+1,2):
        F=lower+i
        C=5*(F-32)/9
        print(f"{F}{C:>6.1f}")
else:
    print("Invalid.")