m=int(input())
for i in range(1,m+1):
    lt="".join(str(x) for x in range(1,i+1))
    s=" "*(2*(m-i))
    rt="".join(str(x) for x in range(i,0,-1))
    print(lt+s+rt)
