def f(n,k,nums):
    cs=sum(nums[:k])
    ms=cs
    for i in range(k,n):
        cs+=nums[i]-nums[i-k]
        ms=max(ms,cs)
    return ms/k
n,k=map(int,input().split())
nums=list(map(int,input().split()))
print(f"{f(n,k,nums):.4f}")
