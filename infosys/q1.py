# Check if an Array Is Sorted 
n= list(map(int, input().split()))
for i in range(1,len(n)):
    if n[i-1]>n[i]:
        print(False)
        exit()
print(True)