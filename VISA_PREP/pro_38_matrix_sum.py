def cs(mat,n):
    rs=[sum(mat[i]) for i in range(n)]
    cs=[sum(mat[j][i] for j in range(n)) for i in range(n)]
    r=[rs[i]+cs[i] for i in range(n)]
    return r
n=int(input())
mat=[]
for _ in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
r=cs(mat,n)
print(*r)
