s=input()
v="aeiouAEIOU"
vc=0
cc=0
for char in s:
    if char.isalpha():
        if char in v:
            vc+=1
        else:
            cc+=1
print(f"{vc},{cc}")
