h=int(input())
for _ in range(h):
    n,m=map(int,input().split())
    if n>m:
        print(n-m)
    else:
        print(0)
