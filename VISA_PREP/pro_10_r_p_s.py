Vignesh,Charan=input().split()
if (Vignesh=='R' and Charan=='S') or (Vignesh=='P' and Charan=='R') or (Vignesh=='S' and Charan=='P'):
    print("Vignesh")
elif (Charan == 'R' and Vignesh=='S')or(Charan=='P'and Vignesh=='R')or(Charan=='S'and Vignesh=='P'):
    print("Charan")
else:
    print("NULL")
