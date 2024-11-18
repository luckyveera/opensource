n=int(input())
arr=list(map(int,input().split()))
x=int(input())
def b(arr,x):
    le,r=0,len(arr)-1
    while le<=r:
        mid=le+(r-le)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            le=mid+1
        else:
            r=mid-1
    return -1
rr=b(arr,x)
print(rr)
