x=int(input())
f=input()
y=int(input())
d={'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y,'/':lambda x,y:x/y if y != 0 else "divided by zero"}
r=d[f](x,y)
if f=='/' and y==0:
    print("divided by zero")
else:
    print(f"{r:.2f}")