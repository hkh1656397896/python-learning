def maxWord(s):
    max=s[0]
    for i in range(1,len(s)):
        if len(max)<=len(s[i]):
            max=s[i]
    return max

s=input()
s=s[:-1].split()
print(maxWord(s))