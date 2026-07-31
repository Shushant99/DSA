arr=[-20,8,-6,-14,0,-19,14,4]
a=len(arr)
a=len(arr)
res=False
for i in range(a):
    for j in range(a):
        if i != j and (i>=0 and j<a) and arr[i]==(2*arr[j]):
            
            res=True
            exit
print(res)