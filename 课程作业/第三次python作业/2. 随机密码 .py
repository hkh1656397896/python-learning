import string
import random
random.seed(10)
L=list(string.ascii_letters)
l=list(map(str,[1,2,3,4,5,6,7,8,9,0]))
M=L+l
n=int(input())
K=[]
for _ in range(n):
    x=random.choice(M)
    K.append(x)
P="".join(K)
print(P)