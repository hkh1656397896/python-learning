m=list(map(int,input("please input a number:")))
if len(m)!=3:
    print("error")
else:
    if m[0]**3+m[1]**3+m[2]**3==m[0]*100+m[1]*10+m[2]:
        print("true")
    else:print("false")


