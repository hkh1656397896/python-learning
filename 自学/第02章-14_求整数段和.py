A,B=map(int,input().split())
if -100<=A<=B<=100:
    x=0
    cnt=0
    for i in range(0,B-A+1):
        a=A+i
        x=x+a
        print(f"{a:>5d}",end="")
        cnt+=1
        if cnt%5==0:
            print()
    if cnt%5!=0:
            print()
    print(f"Sum = {x}")