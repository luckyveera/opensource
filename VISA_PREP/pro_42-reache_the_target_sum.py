c=int(input())
r=[]
for _ in range(c):
    x,y=map(int,input().split())
    rn=(x-y)+1
    r.append(rn)
for result in r:
    print(result)
