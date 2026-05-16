arr=[2,3,4,1,5,6,"a","b", 5,6]
arr1=arr[:len(arr)-1]
arr2=arr[len(arr)-1:]
arr=arr2 + arr1
print(arr)