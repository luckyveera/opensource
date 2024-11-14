n,x,y=map(int,input().split())
if y%x==0 and y<=n*x:
    print("YES")
else:
    print("NO")
