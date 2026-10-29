import math
f=eval(input("time:"))
if f>=10:
    print("50")
elif f<0.5:
    print("0")
else:
    F=math.ceil(f)*5
    print(F)
