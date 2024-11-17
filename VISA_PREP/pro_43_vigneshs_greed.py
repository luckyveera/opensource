d=int(input())
ss=list(map(int,input().split()))
if d<3:
    print(-1)
else:
    ss.sort(reverse=True)
    mm=-1
    for i in range(d-2):
        if ss[i]<ss[i+1]+ss[i+2]:
            mm=ss[i]+ss[i+1]+ss[i+2]
            break
    print(mm)
