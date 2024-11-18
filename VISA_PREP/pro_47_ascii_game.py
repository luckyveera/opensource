s=input()
f=''
for i in s:
    d=ord(i)
    if 97<=d<=122:
        f+=chr(d-32)
    else:
        f+=chr(d+32)
print(f)
