def CountDigit(number,digit):
    cnt=str(number).count(str(digit))
    return cnt
number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)
