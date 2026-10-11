a,b,c=map(int,input().split())
if a+b>c and a+c>b and b+c>a:
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    perimeter=a+b+c
    print(f"area = {area:.2f}; perimeter = {perimeter:.2f}")
else:
    print("These sides do not correspond to a valid triangle")