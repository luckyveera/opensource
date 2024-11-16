def ue(n,arr):
    s=set()
    r=[]
    for num in arr:
        if num not in s:
            r.append(num)
            s.add(num)
    return r
n=int(input())
arr=list(map(int,input().split()))
ur=ue(n,arr)
print(" ".join(map(str,ur)))
