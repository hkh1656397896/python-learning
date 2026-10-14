a,b,c=eval(input("please input three numbers:"))
if int(a)**3+int(b)**3+int(c)**3>1000:
    print(int(a)**3+int(b)**3+int(c)**3-1000)
else:
    print(int(a)+int(b)+int(c))
