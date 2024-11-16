def p(s):
    return "TRUE" if s==s[::-1] else "FALSE"
s=input().strip()
print(p(s))
