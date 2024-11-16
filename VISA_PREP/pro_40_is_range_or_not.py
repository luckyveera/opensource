def c(freq):
    return "YES" if 67 <= freq <=45000 else "NO"
t=int(input())
for _ in range(t):
    x=int(input())
    print(c(x))
