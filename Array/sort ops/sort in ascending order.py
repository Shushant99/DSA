A=[4,5,6,7,6,3,6,7,3,2,5,26,7,8,9]
for i in range(len(A)):
    for j in range(len(A)):
        if A[i]<A[j]:
            
            A[i],A[j]=A[j],A[i]
            

print(A)