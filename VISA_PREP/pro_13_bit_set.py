def im(n,k):
    return (n & (1<<(k-1))) != 0
n=int(input().strip())
k=int(input().strip())
print("true" if im(n,k) else "false")
