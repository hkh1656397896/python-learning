import sys
import re
text=sys.stdin.read().split("#")[0]    
words=re.findall(r"[A-Za-z0-9_]+",text)
cnt={}
for w in words:
    w=w[:15].lower()
    cnt[w]=cnt.get(w,0)+1
print(len(cnt))
items=sorted(cnt.items(),key=lambda kv:(-kv[1],kv[0]))
k=len(cnt)//10
for w,c in items[:k]:
    print(f"{c}:{w}")