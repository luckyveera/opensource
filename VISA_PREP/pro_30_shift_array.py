def r(n,arr):
    ra=arr[1:]+arr[:1]
    return ra
n=int(input())
arr=list(map(int,input().split()))
rr=r(n,arr)
print(" ".join(map(str,rr)))
