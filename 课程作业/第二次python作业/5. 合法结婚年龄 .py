s=input("Sex(F or M):")
a=int(input("Age(1-120):"))
if a<1 or a>120:
    print("Error")
elif s not in ["F","M"]:
    print("Error")
else:
    if s=="F" and a>=20 or s=="M" and a>=22:
        print("Yes")
    else:print("No")