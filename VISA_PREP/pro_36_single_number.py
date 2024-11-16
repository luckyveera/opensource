def fs(arr):
    r=0
    for num in arr:
        r^=num
    return r
n=int(input())
arr=list(map(int,input().split()))
print(fs(arr))
