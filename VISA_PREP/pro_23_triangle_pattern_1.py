y=int(input())
cn=1
for i in range(1,y+1):
    row=[str(cn+j) for j in range(i)]
    print(" ".join(row))
    cn+=i
