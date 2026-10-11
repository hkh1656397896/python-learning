m=input()
n=input()
yes=0
L=[]
for i,ch in enumerate(n):
    if m==ch:
        yes+=1
        L.append(i)
if yes!=0:
    print(f"index = {max(L)}")
if yes==0:
    print("Not Found")
        
