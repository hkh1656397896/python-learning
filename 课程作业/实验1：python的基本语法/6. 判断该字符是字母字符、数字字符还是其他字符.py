import string
L=string.ascii_letters
m=input("please input a char:")
if m in L:
    print("alphabet character")
elif m.isdigit():
    print("digital character")
else:
    print("others character")
