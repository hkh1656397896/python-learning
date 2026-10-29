import re

s = input().strip()
# 一个正则同时管住两条规则：首字符是字母或下划线，之后只能是字母/数字/下划线
if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", s):
    print("Yes")
else:
    print("No")
