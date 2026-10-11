x=float(input())
if x<0:
    print("Invalid Value!")
elif 0<=x<=50:
    print(f"cost = {x*0.53:.2f}")
else:
    print(f"cost = {26.5+(x-50)*0.58:.2f}")
