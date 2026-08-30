def revstring():
    n=list(input())
    l=0
    r=len(n)-1
    while l<r:
        n[l],n[r]=n[r],n[l]
        l+=1
        r-=1
    #list to string
    n=''.join(n)
    print(n)

n=int(input())
for i in range(n):
    revstring()