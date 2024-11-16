def m(n,att):
    mc=0
    cc=0
    for day in att:
        if day==0:
            cc+=1
            mc=max(mc,cc)
        else:
            cc=0
    return mc
n=int(input())
att=list(map(int,input().split()))
print(m(n,att))
