import string
alpha=string.ascii_letters
s=input()
password=[]
for i in s:
    if i in alpha:
        if 65<=ord(i)<=90:
            password.append(chr(155-ord(i)))
        elif 97<=ord(i)<=122:
            password.append(chr(219-ord(i)))
    else:
        password.append(i)
word="".join(password)
print(s)
print(word)






