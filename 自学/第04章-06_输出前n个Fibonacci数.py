N=int(input())
cnt=0
a,b=1,1
if N<1:
    print("Invalid.")
else:
    for _ in range(N):
        cnt+=1
        print(f"{a:11}",end="")
        a,b=b,a+b
        if cnt%5==0:
            print()

