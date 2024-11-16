def c(n):
    cc=n//3
    ccc=n//5
    cccc=n//15
    tc=cc+ccc-cccc
    return tc
n=int(input())
print(c(n))
