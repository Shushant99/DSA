A=[1,2,3,4,5,6]
low=0
target=6
high=len(A)-1
while low<=high:
    mid=(low+high)//2
    if A[mid]==target:
        print(mid)
        break
    elif A[mid]>target:
        high=mid-1
    elif A[mid]<target:
        low=mid+1
    # else:
    #     low=mid+1
else:
    print("not found")