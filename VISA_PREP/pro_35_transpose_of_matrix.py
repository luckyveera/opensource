def t(mat,n):
    tt=[[mat[j][i] for j in range(n)] for i in range(n)]
    return tt
n=int(input())
mat=[]
for _ in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
tt=t(mat,n)
for row in tt:
    print(*row)
