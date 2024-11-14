x,y,z=map(int,input().split())
ttn=x*y
tta=z*1440
if ttn<=tta:
    print("YES")
else:
    print("NO")
