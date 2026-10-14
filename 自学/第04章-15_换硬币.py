m=int(input())
count=0
X=m//5
Y=(m-6)//2
Z=m-6
for x in range(X,0,-1):
    for y in range(Y,0,-1):
        for z in range(Z,0,-1):
            if m==5*x+2*y+z:
                count+=1
                total=x+y+z
                print(f"fen5:{x}, fen2:{y}, fen1:{z}, total:{total}")
print(f"count = {count}")
