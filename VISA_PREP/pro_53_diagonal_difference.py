def diagonalDifference(arr):
    pd=0
    sd=0
    for i in range(len(arr)):
        pd+=arr[i][i]
        sd+=arr[i][len(arr)-i-1]
    return abs(pd-sd)
