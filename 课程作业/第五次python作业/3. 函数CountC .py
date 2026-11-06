import string
def CountC(s):
    alpha=string.ascii_letters
    cnt=0
    for i in s:
        if i in alpha:
            cnt+=1
    return cnt

s=input()
print(CountC(s)) 
