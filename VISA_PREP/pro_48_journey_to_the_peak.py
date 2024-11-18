n=int(input())
y=list(map(int,input().split()))
ca=0
ma=0
for h in y:
    ca+=h
    ma=max(ma,ca)
print(ma)
