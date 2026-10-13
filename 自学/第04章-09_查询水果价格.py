print("[1] apple","[2] pear","[3] orange","[4] grape","[0] exit",sep='\n')
x=list(map(int,input().split()))
L=[1,2,3,4]
K=[]
for i in x:
    if i==0:break
    else:
        K.append(i)
        if len(K)>=5:break
for m in K:   
    if m==1:print("price = 3.00")
    elif m==2:print("price = 2.50")
    elif m==3:print("price = 4.10")
    elif m==4:print("price = 10.20")
    else:print("price = 0.00")
 




