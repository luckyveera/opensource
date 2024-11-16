n=int(input())
g=list(map(int,input().split()))
u=[]
for i in range(n):
    lw=sum(g[:i])
    rw=sum(g[i+1:])
    bb=abs(lw-rw)
    u.append(bb)
print(" ".join(map(str,u)))
    
