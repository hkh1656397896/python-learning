N=int(input())
for _ in range(N):
    x=int(input())
    if x<=1:print("No")
    elif x==2:print("Yes")
    else:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                print("No")
                break
        else:print("Yes")   