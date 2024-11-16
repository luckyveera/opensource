def ri(n):
    reg=n<0
    n=abs(n)
    rii=int(str(n)[::-1])
    if reg:
        rii=-rii
    if rii< -2**31 or rii> 2**31-1:
        return 0
    return rii
n=int(input())
print(ri(n))
