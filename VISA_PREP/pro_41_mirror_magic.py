u=int(input())
mat=[]
for _ in range(u):
    row=list(map(int,input().split()))
    mat.append(row)
mm=[row[::-1] for row in mat]
for row in mm:
    print(*row)
