import re
def acronym(phrase):
    words=re.findall(r"[A-Za-z]+",phrase)
    T=[]
    for w in words:
        w=w[0].upper()
        T.append(w)
    s="".join(T)
    return s
phrase=input()
print(acronym(phrase))
