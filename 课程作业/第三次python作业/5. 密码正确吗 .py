m=input()
if m.isdigit(): 
    n=list(map(int,m))
    for i in range(1,6):
        if n[i]!=(n[i-1]+1)**3%10:
            print("wrong")
            break
    else:print("right")
else:print("wrong")

