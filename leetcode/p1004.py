nums=[0,0,0,1]
k=4
left=0
zeros=0
maxsub=0

for right in range(len(nums)):
    if nums[right]==0:
        zeros+=1
    while zeros>k:
        if nums[left]==0:
            zeros-=1
        left+=1
    maxsub=max(maxsub,right-left+1)

print(maxsub)