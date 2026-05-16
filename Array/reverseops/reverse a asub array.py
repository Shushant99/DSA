arr=[2,3,4,1,5,6,"a","b", 5,6]
a=int(input())
b=int(input())
while a<=b:
    arr[a],arr[b]=arr[b],arr[a]
    a+=1
    b-=1
print(arr)
