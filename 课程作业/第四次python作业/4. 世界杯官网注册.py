import re
m=input()
for i in m:
    if re.fullmatch(r"[a-zA-Z0-9_]",i)==None:
        print("No")
        break
else:
    if m[0].isnumeric():
        print("No")
    else:
        print("Yes")


