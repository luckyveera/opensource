def h(arr,k):
    s=set()
    for num in arr:
        if k-num in s:
            return "true"
        s.add(num)
    return "false"
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
print(h(arr,k))
