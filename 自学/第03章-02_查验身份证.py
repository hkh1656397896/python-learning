N=int(input())
bad=0
for i in range(N):
    v=input().strip()    
    if not v[:17].isdigit():
         print(f"{v}")
         bad+=1
         continue
    V=[int(v[j]) for j in range(17)]
    w=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    weighted_sum=sum(V[j]*w[j] for j in range(17))
    Z=weighted_sum%11 
    M=['1','0','X','9','8','7','6','5','4','3','2']
    m=M[Z]   
    if m!=v[17]:
        print(f"{v}")
        bad+=1
if bad==0:        
    print("All passed")
