error=float(input())
i=1
e=2.0
term=1.0
while term>=error:
    i+=1
    term/=i
    e+=term
    if term<error:
        print(f"{e:.6f}")
        break
