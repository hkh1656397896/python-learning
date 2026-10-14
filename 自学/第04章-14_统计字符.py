import sys
import string
l=b=d=o=0
text=sys.stdin.read()
if text.endswith("\n"):
    text=text[:-1]
    for i in text:
        if i in string.ascii_letters:
            l+=1
        elif i.isdigit():
            d+=1
        elif i in [" ","\n"]:
            b+=1
        else:
            o+=1
        if l+b+d+o>=10:
            break
print(f"letter = {l}, blank = {b}, digit = {d}, other = {o}")