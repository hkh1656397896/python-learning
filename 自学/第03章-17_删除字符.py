m=input().strip()
n=input().strip()
N=n.swapcase()
M=m.replace(n,'').replace(N,'')
x="".join(M)
print(f"result: {x}")

