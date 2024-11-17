p=int(input())
arr=list(map(int,input().split()))
k=int(input())
k%=p
ra=arr[-k:]+arr[:-k]
print(*ra)
