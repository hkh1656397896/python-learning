s=input()
print(s[6:10]+"-"+s[10:12]+"-"+s[12:14])
if int(s[-2])%2==0:
    print("F")
else:
    print("M")
