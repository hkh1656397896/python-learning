h=int(input())
if h>=120:
    Q=120*84.5+(h-120)*84.5*1.15
    print(f"{Q:.2f}")
elif h>=60:
    Q=h*84.5
    print(f"{Q:.2f}")
else:
    Q=h*84.5-700
    print(f"{Q:.2f}")
